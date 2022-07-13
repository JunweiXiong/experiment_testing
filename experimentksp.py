import os
import time
import numpy as np
import subprocess
from matplotlib import pyplot as plt


def find_files():
    haskell_files = {}
    cpp_files = {}
    for root, subdirs, files in os.walk(os.getcwd()):
        parts = root.split("/")
        if len(parts) > 5:
            group = parts[5]
            if group not in haskell_files:
                haskell_files[group] = []
                cpp_files[group] = []
        for file in files:
            if file.endswith(".hf"):
                haskell_files[group].append(root+"/"+file)
            elif file.endswith(".cf"):
                cpp_files[group].append(root+"/"+file)
    for key in haskell_files:
        haskell_files[key].sort()
        cpp_files[key].sort()
    return haskell_files, cpp_files


TIMEOUT = 40


def compare_times(haskell_file, cpp_file):
    with open("temp.txt", "w") as f:
        f.write("sos(formulas).\n")
        with open(cpp_file, "r") as g:
            f.write(g.read() + ".\n")
        f.write("end_of_list.")

    cpp_start = time.time()
    try:
        cpp_result = subprocess.check_output(
            ["/home/users/u6956078/ksp/ksp-0.1.3/ksp", "-c", "/home/users/u6956078/ksp/ksp-0.1.3/conf.files/ordered.conf", "-i", "/home/users/u6956078/mqbf/temp.txt"], timeout=TIMEOUT).decode("utf-8").strip()
    except subprocess.TimeoutExpired:
        cpp_result = "timeout"
    except Exception as e:
        cpp_result = "timeout"
        print("GOT EXCEPTION", e)

    cpp_end = time.time()

    # , haskell_end - haskell_start, haskell_optim_end - haskell_optim_start, cpp_result, haskell_result, haskell_optim_result
    return cpp_end - cpp_start, cpp_result


def run_experiment(haskell_files, cpp_files):
    print("Starting experiment")
    satisfiable = 0
    unsatisfiable = 0

    cpp_times = {}
    haskell_times = {}
    haskell_optim_times = {}
    try:
        for group in haskell_files:
            cpp_times[group] = []
            # haskell_times[group] = []
            # haskell_optim_times[group] = []
            for file1, file2 in zip(haskell_files[group], cpp_files[group]):
                print(file1, file2)
                cpp_time, cpp_result = compare_times(
                    file1, file2)
                results = set(
                    [cpp_result])
                if "timeout" in results:
                    results.remove("timeout")
                if len(results) == 1:
                    cpp_times[group].append(cpp_time)
                    # haskell_times[group].append(haskell_time)
                    # haskell_optim_times[group].append(haskell_optim_time)
                    # if cpp_time < haskell_time and cpp_time < haskell_optim_time:
                    print("KSP won", cpp_time)
                elif len(results) == 0:
                    print("TIMEOUT")
                else:
                    print("BAD RESULTS")
    except KeyboardInterrupt:
        pass
    print("CPP:", cpp_times)
    # print("CPP Stats")
    # print("Min", min(cpp_times))
    # print("Max", max(cpp_times))
    # print("Average", sum(cpp_times) / len(cpp_times))
    # print("Total", sum(cpp_times))

    # print("Haskell Stats")
    # print("Min", min(haskell_times))
    # print("Max", max(haskell_times))
    # print("Average", sum(haskell_times) / len(haskell_times))
    # print("Total", sum(haskell_times))

    # print("Haskell Stats")
    # print("Min", min(haskell_optim_times))
    # print("Max", max(haskell_optim_times))
    # print("Average", sum(haskell_optim_times) / len(haskell_optim_times))
    # print("Total", sum(haskell_optim_times))

    print("SAT", satisfiable, "UNSAT", unsatisfiable)
    return haskell_optim_times, haskell_times, cpp_times


if __name__ == "__main__":
    files = find_files()
    haskell_optim_times, haskell_times, cpp_times = run_experiment(*files)
    # haskell_optim_all = []
    # haskell_all = []
    cpp_all = []
    for group in cpp_times:
        # haskell_optim_all.extend(haskell_optim_times[group])
        # haskell_all.extend(haskell_times[group])
        cpp_all.extend(cpp_times[group])
        print(group)
        # print(haskell_optim_times[group])
        # print(haskell_times[group])
        print(cpp_times[group])

        # h_o_a = np.cumsum(np.sort(
        #     np.array(list(filter(lambda x: x < TIMEOUT, haskell_optim_times[group])))))
        # h_u_a = np.cumsum(
        #     np.sort(np.array(list(filter(lambda x: x < TIMEOUT, haskell_times[group])))))
        c_a = np.cumsum(
            np.sort(np.array(list(filter(lambda x: x < TIMEOUT, cpp_times[group])))))
        plt.figure()
        # plt.plot(h_o_a, np.arange(h_o_a.size), label="Haskell Optimised")
        # plt.plot(h_u_a, np.arange(h_u_a.size), label="Haskell Unoptimised")
        plt.plot(c_a, np.arange(c_a.size), label="KSP")
        plt.xlabel("Time (seconds)")
        plt.legend()
        plt.title(group + " Benchmarks (K)")
        plt.ylabel("Problems Solved")
        plt.savefig("KSP" + group + ".png")
    print("Total")
    # print(haskell_optim_all)
    # print(haskell_all)
    print(cpp_all)
    plt.figure()
    # plt.plot(np.cumsum(np.sort(np.array(haskell_optim_all))),
    #          np.arange(len(haskell_optim_all)), label="Haskell Optimised")
    # plt.plot(np.cumsum(np.sort(np.array(haskell_all))),
    #          np.arange(len(haskell_all)), label="Haskell Unoptimised")
    plt.xlabel("Time (seconds)")
    plt.plot(np.cumsum(np.sort(np.array(cpp_all))),
             np.arange(len(cpp_all)), label="KSP")
    plt.legend()
    plt.title("MQBF Benchmarks")
    plt.ylabel("Problems Solved")
    plt.savefig("KSP" + "overall.png")
