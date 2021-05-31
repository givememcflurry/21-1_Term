# Measure score of Term Project :)


def chk(scr):
    if scr > 0:
        return scr
    else:
        return 0


def lpf(ref_mag, mes_mag, phs):
    mag_err = (abs((mes_mag / ref_mag) - 0.707) / 0.707) * 100  # 1% = -2
    phs_err = (abs(phs - 45) / 45) * 100  # 1% = -0.1

    mag_scr = round(4 - 2.0 * mag_err, 2)
    chk_mag = chk(mag_scr)
    phs_scr = round(4 - 0.1 * phs_err, 2)
    chk_phs = chk(phs_scr)

    print("Mag Error = ", round(mag_err, 3), "& Phs Error = ", round(phs_err, 3))
    print("Mag = ", chk_mag, "& Phs = ", chk_phs)
    print("LPF Score = ", round(chk_mag + chk_phs, 2))


def hpf(ref_mag, mes_mag, phs):
    mag_err = (abs((mes_mag / ref_mag) - 0.707) / 0.707) * 100  # 1% = -2
    phs_err = (abs(phs + 45) / 45) * 100  # 1% = -0.1

    mag_scr = round(4 - 2.0 * mag_err, 2)
    chk_mag = chk(mag_scr)
    phs_scr = round(4 - 0.1 * phs_err, 2)
    chk_phs = chk(phs_scr)

    print("Mag Error = ", round(mag_err, 3), "& Phs Error = ", round(phs_err, 3))
    print("Mag = ", chk_mag, "& Phs = ", chk_phs)
    print("HPF Score = ", round(chk_mag + chk_phs, 2))


def brf(ref_mag, mes_mag, phs):
    mag_err = (abs((mes_mag / ref_mag) - 0.707) / 0.707) * 100  # 1% = -0.05 @ 40%
    phs_err = (abs(phs) / 45) * 100  # 1% = -0.1 @ 20%

    mag_scr = round(2 - 0.05 * mag_err, 2)
    chk_mag = chk(mag_scr)
    phs_scr = round(2 - 0.1 * phs_err, 2)
    chk_phs = chk(phs_scr)

    print("Mag Error = ", round(mag_err, 3), "& Phs Error = ", round(phs_err, 3))
    print("Mag = ", chk_mag, "& Phs = ", chk_phs)
    print("BPF RF Score = ", round(chk_mag + chk_phs, 2))


def bhf(ref_mag, mes_mag, phs):
    mag_err = (abs((mes_mag / ref_mag) - 0.707) / 0.707) * 100  # 1%
    phs_err = (abs(phs - 45) / 45) * 100  # 1%

    mag_scr = round(2 - 0.05 * mag_err, 2)
    chk_mag = chk(mag_scr)
    phs_scr = round(2 - 0.1 * phs_err, 2)
    chk_phs = chk(phs_scr)

    print("Mag Error = ", round(mag_err, 3), "& Phs Error = ", round(phs_err, 3))
    print("Mag = ", chk_mag, "& Phs = ", chk_phs)
    print("BPF HF Score = ", round(chk_mag + chk_phs, 2))


def blf(ref_mag, mes_mag, phs):
    mag_err = (abs((mes_mag / ref_mag) - 0.707) / 0.707) * 100  # 1%
    phs_err = (abs(phs + 45) / 45) * 100  # 1%

    mag_scr = round(2 - 0.05 * mag_err, 2)
    chk_mag = chk(mag_scr)
    phs_scr = round(2 - 0.1 * phs_err, 2)
    chk_phs = chk(phs_scr)

    print("Mag Error = ", round(mag_err, 3), "& Phs Error = ", round(phs_err, 3))
    print("Mag = ", chk_mag, "& Phs = ", chk_phs)
    print("BPF LF Score = ", round(chk_mag + chk_phs, 2))
