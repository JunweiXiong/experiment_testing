import ast
import matplotlib.pylab as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
TIMEOUT = 40


# with open("k_results.txt", "r") as f:
#     for line in f:
#         if line[:4] == "CPP:":
#             cpp_times = ast.literal_eval(line[5:].strip())
#         elif line[:6] == "Unhas:":
#             haskell_times = ast.literal_eval(line[7:].strip())
#         elif line[:6] == "OpHas:":
#             haskell_optim_times = ast.literal_eval(line[7:].strip())

# haskell_optim_all = []
# haskell_all = []
# cpp_all = []
# for group in cpp_times:
#     haskell_optim_all.extend(haskell_optim_times[group])
#     haskell_all.extend(haskell_times[group])
#     cpp_all.extend(cpp_times[group])
#     print(group)
#     print(haskell_optim_times[group])
#     print(haskell_times[group])
#     print(cpp_times[group])

#     h_o_a = np.cumsum(np.sort(
#         np.array(list(filter(lambda x: x < TIMEOUT, haskell_optim_times[group])))))
#     h_u_a = np.cumsum(
#         np.sort(np.array(list(filter(lambda x: x < TIMEOUT, haskell_times[group])))))
#     c_a = np.cumsum(
#         np.sort(np.array(list(filter(lambda x: x < TIMEOUT, cpp_times[group])))))
#     plt.figure()
#     plt.plot(h_o_a, np.arange(h_o_a.size), label="Haskell Optimised")
#     plt.plot(h_u_a, np.arange(h_u_a.size), label="Haskell Unoptimised")
#     plt.plot(c_a, np.arange(c_a.size), label="C++")
#     plt.xlabel("Time (seconds)", fontsize=12)
#     plt.legend(prop={"size": 12})
#     plt.title(group + " Benchmarks (K)", fontsize=16)
#     plt.ylabel("Problems Solved", fontsize=12)
#     plt.xscale('log', base=2)
#     plt.savefig("final/K" + group + "_final.png")
# print("Total")
# print(haskell_optim_all)
# print(haskell_all)
# print(cpp_all)
# plt.figure()
# plt.plot(np.cumsum(np.sort(np.array(haskell_optim_all))),
#          np.arange(len(haskell_optim_all)), label="Haskell Optimised")
# plt.plot(np.cumsum(np.sort(np.array(haskell_all))),
#          np.arange(len(haskell_all)), label="Haskell Unoptimised")
# plt.xlabel("Time (seconds)", fontsize=12)
# plt.plot(np.cumsum(np.sort(np.array(cpp_all))),
#          np.arange(len(cpp_all)), label="C++")
# plt.legend(prop={"size": 12})
# plt.title("MQBF Benchmarks (K)", fontsize=16)
# plt.ylabel("Problems Solved", fontsize=12)
# plt.xscale('log', base=2)
# plt.savefig("final/K" + "overall_final.png")

with open("t_results.txt", "r") as f:
    for line in f:
        if line[:4] == "CPP:":
            cpp_times = ast.literal_eval(line[5:].strip())
        elif line[:6] == "Unhas:":
            haskell_times = ast.literal_eval(line[7:].strip())
        elif line[:6] == "OpHas:":
            haskell_optim_times = ast.literal_eval(line[7:].strip())

haskell_optim_all = []
haskell_all = []
cpp_all = []
for group in cpp_times:
    haskell_optim_all.extend(haskell_optim_times[group])
    haskell_all.extend(haskell_times[group])
    cpp_all.extend(cpp_times[group])
    print(group)
    print(haskell_optim_times[group])
    print(haskell_times[group])
    print(cpp_times[group])

    h_o_a = np.cumsum(np.sort(
        np.array(list(filter(lambda x: x < TIMEOUT, haskell_optim_times[group])))))
    h_u_a = np.cumsum(
        np.sort(np.array(list(filter(lambda x: x < TIMEOUT, haskell_times[group])))))
    c_a = np.cumsum(
        np.sort(np.array(list(filter(lambda x: x < TIMEOUT, cpp_times[group])))))
    fig = plt.figure()
    plt.plot(h_o_a, np.arange(h_o_a.size), label="Haskell Optimised")
    plt.plot(h_u_a, np.arange(h_u_a.size), label="Haskell Unoptimised")
    plt.plot(c_a, np.arange(c_a.size), label="C++")
    plt.xlabel("Time (seconds)", fontsize=12)
    plt.legend(prop={"size": 12})
    plt.title(group + " Benchmarks (T)", fontsize=16)
    plt.ylabel("Problems Solved", fontsize=12)
    plt.xscale('log', base=2)
    plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
    fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
    plt.savefig("finalfinal/T" + group + "_final.png")

    other_hoa = []
    other_hua = []
    other_ca = []
    xs = []
    for i in range(-4, 6):
        time_limit = 2 ** i
        xs.append(time_limit)
        def f_time_limit(x): return x < time_limit
        other_hoa.append(
            len(list(filter(f_time_limit, haskell_optim_times[group]))))
        other_hua.append(
            len(list(filter(f_time_limit, haskell_times[group]))))
        other_ca.append(
            len(list(filter(f_time_limit, cpp_times[group]))))

    fig = plt.figure()
    plt.plot(xs, other_hoa, label="Haskell Optimised")
    plt.plot(xs, other_hua, label="Haskell Unoptimised")
    plt.plot(xs, other_ca, label="C++")
    plt.xlabel("Time (seconds)", fontsize=12)
    plt.legend(prop={"size": 12})
    plt.title(group + " Benchmarks (T)", fontsize=16)
    plt.ylabel("Problems Solved", fontsize=12)
    plt.xscale('log', base=2)
    plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
    fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
    plt.savefig("finalfinal/newT" + group + "_final.png")
print("Total")
print(haskell_optim_all)
print(haskell_all)
print(cpp_all)

average_time_hoa = (sum(filter(lambda x: x < 40, haskell_optim_all))
                    ) / len(list(filter(lambda x: x < 40, haskell_optim_all)))
average_time_hua = (sum(filter(lambda x: x < 40, haskell_all))) / \
    len(list(filter(lambda x: x < 40, haskell_all)))
average_time_cpp = (sum(filter(lambda x: x < 40, cpp_all))) / \
    len(list(filter(lambda x: x < 40, cpp_all)))

fig = plt.figure()
plt.bar(np.arange(3), [average_time_hoa, average_time_hua, average_time_cpp])
plt.xlabel("Prover")
plt.ylabel("Average Time (seconds)")
plt.title("Average Time to Solve MQBF (T) Benchmarks")
plt.xticks(np.arange(3), ["Optimised Haskell", "Unoptimised Haskell", "C++"])
for index, value in enumerate([average_time_hoa, average_time_hua, average_time_cpp]):
    plt.text(index-0.14, value+0.05, "{: .2f}".format(round(value, 2)))
plt.savefig("barT.png")
print(average_time_hoa, average_time_hua, average_time_cpp)

haskell_optim_all = list(filter(lambda x: x < 1, haskell_optim_all))
haskell_all = list(filter(lambda x: x < 1, haskell_all))
cpp_all = list(filter(lambda x: x < 1, cpp_all))

print("THaskell Optim", len(haskell_optim_all))
print("THaskell Unoptim", len(haskell_all))
print("TCPP", len(cpp_all))

fig = plt.figure()
plt.plot(np.cumsum(np.sort(np.array(haskell_optim_all))),
         np.arange(len(haskell_optim_all)), label="Haskell Optimised")
plt.plot(np.cumsum(np.sort(np.array(haskell_all))),
         np.arange(len(haskell_all)), label="Haskell Unoptimised")
plt.xlabel("Time (seconds)", fontsize=12)
plt.plot(np.cumsum(np.sort(np.array(cpp_all))),
         np.arange(len(cpp_all)), label="C++")
plt.legend()
plt.title("MQBF Benchmarks (T)", fontsize=16)
plt.ylabel("Problems Solved", fontsize=12)
plt.xscale('log', base=2)
plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
plt.savefig("finalfinal/T" + "overall_final.png")

other_hoa = []
other_hua = []
other_ca = []
xs = []
for i in range(-4, 6):
    time_limit = 2 ** i
    xs.append(time_limit)

    def f_time_limit(x): return x <= time_limit
    other_hoa.append(
        len(list(filter(f_time_limit, haskell_optim_all))))
    other_hua.append(
        len(list(filter(f_time_limit, haskell_all))))
    other_ca.append(
        len(list(filter(f_time_limit, cpp_all))))

fig = plt.figure()
plt.plot(xs, other_hoa, label="Haskell Optimised")
plt.plot(xs, other_hua, label="Haskell Unoptimised")
plt.plot(xs, other_ca, label="C++")
plt.xlabel("Time (seconds)", fontsize=12)
plt.legend(prop={"size": 12})
plt.title("MQBF Benchmarks (T)", fontsize=16)
plt.ylabel("Problems Solved", fontsize=12)
plt.xscale('log', base=2)
plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
plt.savefig("finalfinal/newT" + "overall_final.png")


with open("k_results.txt", "r") as f:
    for line in f:
        if line[:4] == "CPP:":
            cpp_times = ast.literal_eval(line[5:].strip())
            # for group in cpp_times:
            #     cpp_times[group] = list(
            #         map(lambda x: x if x < 16 else 0.8 * x, cpp_times[group]))
        elif line[:6] == "Unhas:":
            haskell_times = ast.literal_eval(line[7:].strip())
        elif line[:6] == "OpHas:":
            haskell_optim_times = ast.literal_eval(line[7:].strip())

with open("outksp2.txt", "r") as f:
    for line in f:
        if line[:4] == "CPP:":
            ksp_times = ast.literal_eval(line[5:].strip())
            # def f(x): return x if x < 8 else (
            #     x * 1.5 if x < 16 else x*2.2)
            # for group in ksp_times:
            #     ksp_times[group] = list(
            #         map(f, ksp_times[group]))


haskell_optim_all = []
haskell_all = []
cpp_all = []
ksp_all = []
for group in cpp_times:
    haskell_optim_all.extend(haskell_optim_times[group])
    haskell_all.extend(haskell_times[group])
    cpp_all.extend(cpp_times[group])
    ksp_all.extend(ksp_times[group])
    # print(group)
    # print(haskell_optim_times[group])
    # print(haskell_times[group])
    # print(cpp_times[group])
    # print(ksp_times[group])

    h_o_a = np.cumsum(np.sort(
        np.array(list(filter(lambda x: x < TIMEOUT, haskell_optim_times[group])))))
    h_u_a = np.cumsum(
        np.sort(np.array(list(filter(lambda x: x < TIMEOUT, haskell_times[group])))))
    c_a = np.cumsum(
        np.sort(np.array(list(filter(lambda x: x < TIMEOUT, cpp_times[group])))))
    k_a = np.cumsum(
        np.sort(np.array(list(filter(lambda x: x < TIMEOUT, ksp_times[group])))))

    fig = plt.figure()
    plt.plot(h_o_a, np.arange(h_o_a.size), label="Haskell Optimised")
    plt.plot(h_u_a, np.arange(h_u_a.size), label="Haskell Unoptimised")
    plt.plot(c_a, np.arange(c_a.size), label="C++")
    plt.plot(k_a, np.arange(k_a.size), label="KSP")
    plt.xlabel("Time (seconds)", fontsize=12)
    plt.legend(prop={"size": 12})
    plt.title(group + " Benchmarks (K)", fontsize=16)
    plt.ylabel("Problems Solved", fontsize=12)
    plt.xscale('log', base=2)
    fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
    plt.savefig("finalfinal/K" + group + "_final.png")

    other_hoa = []
    other_hua = []
    other_ca = []
    other_ka = []
    xs = []
    for i in range(-4, 6):
        time_limit = 2 ** i
        xs.append(time_limit)
        def f_time_limit(x): return x <= time_limit
        other_hoa.append(
            len(list(filter(f_time_limit, haskell_optim_times[group]))))
        other_hua.append(
            len(list(filter(f_time_limit, haskell_times[group]))))

        other_ca.append(
            len(list(filter(f_time_limit, cpp_times[group]))))

        other_ka.append(
            len(list(filter(f_time_limit, ksp_times[group]))))

    fig = plt.figure()
    plt.plot(xs, other_hoa, label="Haskell Optimised")
    plt.plot(xs, other_hua, label="Haskell Unoptimised")
    plt.plot(xs, other_ca, label="C++")
    plt.plot(xs, other_ka, label="KSP")
    plt.xlabel("Time (seconds)", fontsize=12)
    plt.legend(prop={"size": 12})
    plt.title(group + " Benchmarks (K)", fontsize=16)
    plt.ylabel("Problems Solved", fontsize=12)
    plt.xscale('log', base=2)
    plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
    fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
    plt.savefig("finalfinal/newK" + group + "_final.png")
print("Total")
# print(haskell_optim_all)
# print(haskell_all)
# print(cpp_all)
# print(ksp_all)
print("Accumalated time")
average_time_hoa = (sum(filter(lambda x: x < 40, haskell_optim_all))
                    ) / len(list(filter(lambda x: x < 40, haskell_optim_all)))
average_time_hua = (sum(filter(lambda x: x < 40, haskell_all))) / \
    len(list(filter(lambda x: x < 40, haskell_all)))
average_time_cpp = (sum(filter(lambda x: x < 40, cpp_all))) / \
    len(list(filter(lambda x: x < 40, cpp_all)))
average_time_ksp = (sum(filter(lambda x: x < 40, ksp_all))) / \
    len(list(filter(lambda x: x < 40, ksp_all)))

fig = plt.figure(figsize=(16, 9))
plt.bar(np.arange(4), [average_time_hoa,
        average_time_hua, average_time_cpp, average_time_ksp])
plt.xlabel("Prover")
plt.ylabel("Average Time (seconds)")
plt.title("Average Time to Solve MQBF (K) Benchmarks")
plt.xticks(np.arange(4), ["Optimised\nHaskell",
           "Unoptimised\nHaskell", "C++", "KSP"])
for index, value in enumerate([average_time_hoa, average_time_hua, average_time_cpp, average_time_ksp]):
    plt.text(index-0.17, value+0.02, "{: .2f}".format(round(value, 2)))
plt.savefig("barK.png")

print(average_time_hoa, average_time_hua, average_time_cpp, average_time_ksp)

haskell_optim_all = list(filter(lambda x: x < 1, haskell_optim_all))
haskell_all = list(filter(lambda x: x < 1, haskell_all))
cpp_all = list(filter(lambda x: x < 1, cpp_all))
ksp_all = list(filter(lambda x: x < 1, ksp_all))
print("Haskell Optim", len(haskell_optim_all))
print("Haskell Unoptim", len(haskell_all))
print("CPP", len(cpp_all))
print("KSP", len(ksp_all))
fig = plt.figure()
plt.plot(np.cumsum(np.sort(np.array(haskell_optim_all))),
         np.arange(len(haskell_optim_all)), label="Haskell Optimised")
plt.plot(np.cumsum(np.sort(np.array(haskell_all))),
         np.arange(len(haskell_all)), label="Haskell Unoptimised")
plt.xlabel("Time (seconds)", fontsize=12)
plt.plot(np.cumsum(np.sort(np.array(cpp_all))),
         np.arange(len(cpp_all)), label="C++")
plt.plot(np.cumsum(np.sort(np.array(ksp_all))),
         np.arange(len(ksp_all)), label="KSP")
plt.legend()
plt.title("MQBF Benchmarks (K)", fontsize=16)
plt.ylabel("Problems Solved", fontsize=12)
plt.xscale('log', base=2)
fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
plt.savefig("finalfinal/K" + "overall_final.png")


other_hoa = []
other_hua = []
other_ca = []
other_ka = []
xs = []
for i in range(-4, 6):
    time_limit = 2 ** i
    xs.append(time_limit)
    def f_time_limit(x): return x <= time_limit
    other_hoa.append(
        len(list(filter(f_time_limit, haskell_optim_all))))
    other_hua.append(
        len(list(filter(f_time_limit, haskell_all))))
    other_ca.append(
        len(list(filter(f_time_limit, cpp_all))))
    other_ka.append(
        len(list(filter(f_time_limit, ksp_all))))

fig = plt.figure()
plt.plot(xs, other_hoa, label="Haskell Optimised")
plt.plot(xs, other_hua, label="Haskell Unoptimised")
plt.plot(xs, other_ca, label="C++")
plt.plot(xs, other_ka, label="KSP")
plt.xlabel("Time (seconds)", fontsize=12)
plt.legend(prop={"size": 12})
plt.title("MQBF Benchmarks (K)", fontsize=16)
plt.ylabel("Problems Solved", fontsize=12)
plt.xscale('log', base=2)
plt.xticks([0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32])
fig.axes[0].get_xaxis().set_major_formatter(ScalarFormatter())
plt.savefig("finalfinal/newK" + "overall_final.png")

haskell_optim_all = list(filter(lambda x: x < 40, haskell_optim_all))
haskell_all = list(filter(lambda x: x < 40, haskell_all))
cpp_all = list(filter(lambda x: x < 40, cpp_all))
ksp_all = list(filter(lambda x: x < 40, ksp_all))
