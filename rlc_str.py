# 2021-1 Device-Value Calculate Module :)
# Strict device value version

import math as mt

res_list = [0.001, 0.0022, 0.0033, 0.0047, 0.0056, 0.0068, 0.0075, 0.0091, 0.01, 0.022, 0.033, 0.051, 0.082, 0.1, 0.22,
            0.33, 0.47, 0.56, 0.68, 0.82, 1]  # kilo Ohm
ind_list = [0.22, 0.33, 0.47, 0.56, 0.68, 0.82, 1, 1.2, 1.5, 2.7, 3.3, 4.7, 10, 22, 33, 68]  # milli Henri
cap_list = [0.033, 0.047, 0.068, 0.1, 0.12, 0.15, 0.18, 0.22, 0.33, 0.47, 0.56, 0.68]  # micro Farad


def bbc(res, ind):  # BPF BW Calculate
    input_res = res * 1e+3
    input_ind = ind * 1e-3
    pi = 3.141592
    bwf = input_res / (2 * pi * input_ind)
    return bwf


def rfc(ind, cap):  # Resonant Freq. Calculate
    input_ind = ind * 1e-3
    input_cap = cap * 1e-6
    pi = 3.141592
    rsf = 1 / (2 * pi * mt.sqrt(input_ind * input_cap))
    return rsf


def bbd():  # BPF BW Device-value calculate
    fb = 2000  # Band Width Feq = 2kHz
    dif = 9999
    res_num = len(res_list)
    ind_num = len(ind_list)
    rc, ic = 0, 0
    res_save, ind_save = 0, 0
    while rc < res_num:
        while ic < ind_num:
            bbd_bwf = bbc(res_list[rc], ind_list[ic])
            if abs(bbd_bwf - fb) < dif:
                dif = abs(bbd_bwf - fb)
                res_save = res_list[rc]
                ind_save = ind_list[ic]
            ic = ic + 1
        rc = rc + 1
        ic = 0
    print("R = ", res_save, "kOhm")
    print("L = ", ind_save, "mH")
    print("BW = ", round(bbc(res_save, ind_save)))


def per(std_freq, chk_freq):  # Difference Percentage
    per_dif = abs(std_freq - chk_freq) / std_freq * 100
    return per_dif


def bnr(input_fb, input_fr):  # ★find device-value from BW & Resonant freq.★
    fb = input_fb  # Band Width Feq = 2kHz
    fr = input_fr  # Resonant Freq. = 3kHz
    res_num = len(res_list)
    ind_num = len(ind_list)
    cap_num = len(cap_list)
    rc, ic, cc = 0, 0, 0
    res_save, ind_save, cap_save = 0, 0, 0
    dif = 1000
    while rc < res_num:
        while ic < ind_num:
            while cc < cap_num:
                bbd_bwf = bbc(res_list[rc], ind_list[ic])
                rfc_rsf = rfc(ind_list[ic], cap_list[cc])

                per_bwf = per(fb, bbd_bwf)
                per_ref = per(fr, rfc_rsf)

                cal_per = mt.pow(per_bwf, 2) + mt.pow(per_ref, 2)

                if abs(cal_per) < dif:
                    dif = cal_per
                    res_save = res_list[rc]
                    ind_save = ind_list[ic]
                    cap_save = cap_list[cc]

                cc = cc + 1
            ic = ic + 1
            cc = 0
        rc = rc + 1
        ic = 0

    print("R = ", res_save, "kOhm")
    print("L = ", ind_save, "mH")
    print("C = ", cap_save, "uF")
    print("BW = ", round(bbc(res_save, ind_save)), " RF = ", round(rfc(ind_save, cap_save)))


def bnr_test(input_fb, input_fr):
    fb = input_fb  # Band Width Feq = 2kHz
    fr = input_fr  # Resonant Freq. = 3kHz
    res_num = len(res_list)
    ind_num = len(ind_list)
    cap_num = len(cap_list)
    rc, ic, cc = 0, 0, 0
    while rc < res_num:
        while ic < ind_num:
            while cc < cap_num:
                bbd_bwf = bbc(res_list[rc], ind_list[ic])
                rfc_rsf = rfc(ind_list[ic], cap_list[cc])

                per_bwf = per(fb, bbd_bwf)
                per_ref = per(fr, rfc_rsf)

                cal_per = mt.pow(per_bwf, 2) + mt.pow(per_ref, 2)

                print("R = ", res_list[rc], "kOhm")
                print("L = ", ind_list[ic], "mH")
                print("C = ", cap_list[cc], "uF")
                print("BW = ", bbc(res_list[rc], ind_list[ic]), " RF = ", rfc(ind_list[ic], cap_list[cc]))
                print("Per = ", cal_per)

                cc = cc + 1
            ic = ic + 1
            cc = 0
        rc = rc + 1
        ic = 0


def bnr_test2(unit_fb, unit_fr):  # Consider all of probability
    cnt = 1
    std_fb = 2000
    std_fr = 3000
    while cnt < 11:
        input_fb = (unit_fb * cnt) + std_fb
        input_fr = (unit_fr * cnt) + std_fr
        bnr(input_fb, input_fr)
        cnt = cnt + 1


def lcc(res, cap):  # LPF Cutoff-Freq. Calculate
    input_res = res * 1e+3
    input_cap = cap * 1e-6
    pi = 3.141592
    lfc = 1 / (2 * pi * input_res * input_cap)
    return lfc


def frc(input_freq):  # ★Find Res, Cap - LPF★
    fcl = input_freq
    dif = 1e+5
    res_num = len(res_list)
    cap_num = len(cap_list)
    rc, cc = 0, 0
    res_save, cap_save = 0, 0
    while rc < res_num:
        while cc < cap_num:
            lcc_lfc = lcc(res_list[rc], cap_list[cc])

            if abs(lcc_lfc - fcl) < dif:
                dif = abs(lcc_lfc - fcl)
                res_save = res_list[rc]
                cap_save = cap_list[cc]

            cc = cc + 1
        rc = rc + 1
        cc = 0
    print("R = ", res_save, "kOhm")
    print("C = ", cap_save, "uF")
    print("LPF_Fc = ", round(lcc(res_save, cap_save)))


def frc_test():
    i = 1
    frq = 500
    while i < 11:
        frc(i * frq)
        i = i + 1


def hcc(res, ind):  # HPF Cutoff-Freq. Calculate
    input_res = res * 1e+3
    input_ind = ind * 1e-3
    pi = 3.141592
    hfc = input_res / (2 * pi * input_ind)
    return hfc


def fri(input_freq):  # ★Find Res, Ind - HPF★
    fch = input_freq
    dif = 1e+5
    res_num = len(res_list)
    ind_num = len(ind_list)
    rc, ic = 0, 0
    res_save, ind_save = 0, 0
    while rc < res_num:
        while ic < ind_num:
            hcc_hfc = hcc(res_list[rc], ind_list[ic])

            if abs(hcc_hfc - fch) < dif:
                dif = abs(hcc_hfc - fch)
                res_save = res_list[rc]
                ind_save = ind_list[ic]

            ic = ic + 1
        rc = rc + 1
        ic = 0
    print("R = ", res_save, "kOhm")
    print("L = ", ind_save, "mH")
    print("HPF_Fc = ", round(hcc(res_save, ind_save)))


def fri_test():
    i = 1
    frq = 400
    while i < 11:
        fri(i * frq)
        i = i + 1
