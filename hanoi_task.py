def req_steps(num_disks):
    if num_disks == 1:
        return 1

    else:
        return 2 * (req_steps(num_disks - 1)) + 1

    return -1
