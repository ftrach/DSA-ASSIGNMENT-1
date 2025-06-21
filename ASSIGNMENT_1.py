import random, time, matplotlib.pyplot as plt

# BUBBLE SORT FUNCTION - COMPARES AND SWAPS ADJACENT ELEMENTS TO "BUBBLE" LARGEST TO THE END

def s_b(a):
    c = 0  # INITIALIZE OPERATION COUNTER
    
    for i in range(len(a) - 1):  # OUTER LOOP FOR PASSES
    
        for j in range(len(a) - 1 - i):  # INNER LOOP FOR COMPARISON
        
            c += 1  # COUNT COMPARISON
            if a[j] > a[j + 1]:  # IF ELEMENTS ARE OUT OF ORDER, SWAP THEM
                a[j], a[j + 1] = a[j + 1], a[j]
                c += 3  # COUNT SWAP AS 3 OPERATIONS
    return c  # RETURN TOTAL OPERATION COUNT




# SELECTION SORT FUNCTION - FINDS MINIMUM ELEMENT IN UNSORTED PART AND PLACES IT AT THE FRONT

def s_s(a):
    c = 0  # INITIALIZE OPERATION COUNTER
    for i in range(len(a)):
        m = i  # SET CURRENT INDEX AS MINIMUM
        for j in range(i + 1, len(a)):
            c += 1  # COUNT COMPARISON
            if a[j] < a[m]: m = j  # UPDATE MINIMUM INDEX
        if m != i:
            a[i], a[m] = a[m], a[i]  # SWAP MINIMUM WITH FIRST UNSORTED ELEMENT
            c += 3  # COUNT SWAP
    return c



# INSERTION SORT FUNCTION - INSERTS EACH ELEMENT INTO ITS CORRECT POSITION IN A SORTED SUBLIST

def s_i(a):
    c = 0
    for i in range(1, len(a)):
        k = a[i]  # STORE CURRENT VALUE
        j = i - 1
        while j >= 0 and k < a[j]:  # SHIFT LARGER ELEMENTS TO THE RIGHT
            a[j + 1] = a[j]
            j -= 1
            c += 2  # COUNT SHIFT + COMPARISON
        a[j + 1] = k  # INSERT ELEMENT IN CORRECT POSITION
        c += 1
    return c



# RANGE-BASED INSERTION SORT FOR PARTIAL LIST

def s_r(a, l, h):
    c = 0
    for i in range(l + 1, h + 1):
        k = a[i]
        j = i - 1
        while j >= l and k < a[j]:  # SHIFT ELEMENTS IN RANGE
            a[j + 1] = a[j]
            j -= 1
            c += 2
        a[j + 1] = k
        c += 1
    return c



# QUICK SORT FUNCTION - DIVIDES ARRAY USING PIVOT AND RECURSIVELY SORTS PARTS


def s_q(a):
    c = 0
    z = [(0, len(a) - 1)]  # STACK FOR MANUAL RECURSION
    while z:
        l, h = z.pop()
        if l < h:
            p, s = p_x(a, l, h)  # PARTITION ARRAY AND GET PIVOT
            c += s  # ADD PARTITION STEP COUNT
            z += [(l, p - 1), (p + 1, h)]  # PUSH LEFT AND RIGHT SEGMENTS TO STACK
    return c




# PARTITION FUNCTION - REARRANGES ELEMENTS AROUND A PIVOT


def p_x(a, l, h):
    c = 0
    x = a[h]  # CHOOSE LAST ELEMENT AS PIVOT
    i = l - 1
    for j in range(l, h):  # COMPARE EACH ELEMENT TO PIVOT
        c += 1
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]  # MOVE SMALLER ELEMENT TO THE LEFT
            c += 3
    a[i + 1], a[h] = a[h], a[i + 1]  # PLACE PIVOT IN CORRECT POSITION
    c += 3
    return i + 1, c



# FUNCTION TO GENERATE A REVERSE-SORTED LIST - WORST CASE FOR MOST ALGORITHMS

def g(n): return list(range(n, 0, -1))



# FUNCTION TO PLOT DATA USING MATPLOTLIB

def p(d, s, t, y, f):
    for k, v in d.items(): plt.plot(s, v, label=k)
    plt.title(t)  # TITLE OF PLOT
    plt.xlabel("SIZE")  # X-AXIS LABEL
    plt.ylabel(y)  # Y-AXIS LABEL
    plt.legend()  # SHOW LEGEND
    plt.grid()  # ADD GRID
    plt.tight_layout()  # OPTIMIZE LAYOUT
    plt.savefig(f)  # SAVE TO FILE
    plt.clf()  # CLEAR PLOT



# FUNCTION TO MEASURE EXECUTION TIME OF A FUNCTION CALL

def t(f, *a):
    s = time.time()
    f(*a)
    return time.time() - s  # RETURN ELAPSED TIME



# MAIN FUNCTION TO RUN SORTS ON DIFFERENT SIZES, RECORD T(n) AND TIME, THEN PLOT

def x():
    sz = [10, 50, 100, 500, 1000]  # LIST SIZES TO TEST
    ops = {"b": [], "s": [], "i": [], "q": [], "r": []}  # STEP COUNTS
    tm = {"b": [], "s": [], "i": [], "q": [], "r": []}  # EXECUTION TIMES

    for n in sz:
        a = g(n)  # GENERATE WORST CASE LIST


        # STORE T(n) FOR EACH ALGORITHM

        ops["b"].append(s_b(a.copy()))
        ops["s"].append(s_s(a.copy()))
        ops["i"].append(s_i(a.copy()))
        ops["q"].append(s_q(a.copy()))
        ops["r"].append(s_r(a.copy(), 0, len(a) - 1))


        # STORE EXECUTION TIME FOR EACH ALGORITHM

        tm["b"].append(t(s_b, a.copy()))
        tm["s"].append(t(s_s, a.copy()))
        tm["i"].append(t(s_i, a.copy()))
        tm["q"].append(t(s_q, a.copy()))
        tm["r"].append(t(s_r, a.copy(), 0, len(a) - 1))


    # PRINT OPERATION COUNTS AND TIME RESULTS

    print("T(n):")
    [print(k, v) for k, v in ops.items()]
    print("\nTime:")
    [print(k, v) for k, v in tm.items()]
    

    # GENERATE PLOTS AND SAVE TO FILES
    
    p(ops, sz, "T(n) VS SIZE", "STEPS", "t_n_vs_n.png")
    p(tm, sz, "TIME VS SIZE", "SECONDS", "time_vs_n.png")



# START EXECUTION


if __name__ == "__main__": x()
