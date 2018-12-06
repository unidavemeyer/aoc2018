# solutions to various advent-of-code problems

import re
import sys

# NOTE (davidm) this is BillRo's trick -- put all of the input strings into a simple python file
#  that is then imported here, so that the input is readily available, but also doesn't clutter up
#  the code. Didn't bother to extract the input for day1, so that's inline below.

import aoc2018in as ain



def Sum(lG):
    g0 = 0.0
    for g1 in lG:
        g0 += g1

    return g0

def Day1a():
    """Expects input of form ((+|-)N *)* and is to sum up all of those values starting from
    zero and return the result."""

    strIn = '''
    -10 +18 +5 +1 +1 -19 -13 -4 -4 -5 -17 +13 -3 +18 -17 +14 +11 +14 +16 +6 -2 -3 -3 -5 +18 +17 -9 +14 +13 +3 -17 -3 +11 -4 -5 +3 +9 -20 -18 +10 +1 +1 -14
    +9 -5 +20 -6 +1 +2 +2 -13 -11 +18 +18 +1 +2 -11 +23 +2 -7 +2 +7 -3 +6 +9 +8 +13 -8 +12 +7 +4 +9 -11 -19 +1 +13 +15 -14 +10 +19 -6 +1 +7 -14 +3 +17 +2 +2
    +15 +15 +18 +6 -9 +8 +15 +12 +15 +5 +8 +1 +6 -13 +18 +10 +10 +7 +14 +4 +9 +17 +10 +6 +7 +9 +5 +1 +1 +19 +10 +18 -5 +10 +7 -6 -10 +17 -12 -15 -17 +5 +7 -11 +18
    -12 -12 -3 +10 -4 -5 +13 +10 -1 +7 -12 -11 -9 -18 +3 -1 -15 -7 -15 +4 -7 -4 -7 +19 -3 +14 +9 -11 -7 +16 -10 -3 +10 +13 +10 -7 +13 +11 +17 +7 +4 +20 +19 -1 -5
    +10 +7 -9 -14 -3 -15 +5 -19 +13 +9 -12 -6 -13 -15 -2 -15 -3 +11 +22 +19 +18 -6 +10 -9 +10 +19 -15 -2 +20 +12 -20 -8 +23 +15 -11 +10 -2 +8 -4 -19 +16 +16 -6 -22
    -2 +9 +13 -19 +8 +16 +18 +21 +17 +26 -19 +16 +8 -14 -1 +8 +9 +2 +6 +4 -7 -2 +1 +14 -3 +17 +6 +19 -14 +10 +13 -17 -10 +11 -14 -13 -13 +11 +19 +18 +1 -12 +14 -17 +8
    +11 +1 +15 +13 -12 +14 +2 -8 +9 +9 +2 +14 +7 +14 -1 -11 +13 -11 -3 -18 +7 -19 -1 -14 +4 -11 +12 -6 -19 +6 +15 -10 -9 +24 -9 -1 +14 +8 -5 -5 +12 +16 -14 +3 -6 +12
    +11 -18 +9 +17 +10 +11 -19 +13 +9 +4 +15 +8 -21 +5 -12 +4 +13 +13 +6 +1 +6 +4 +6 -14 -6 +17 -4 +10 +13 +17 +3 -5 +19 +6 -16 -8 +21 -19 +4 -15 -5 +7 -11 -19 +18 -2
    +10 -17 -8 -8 -10 +7 -19 -6 -11 +19 +5 +9 -11 +16 -13 -17 +5 -18 -1 +12 -9 -18 +25 -3 -8 -15 +9 -19 -5 +18 +5 +3 -1 -12 -12 +8 -21 +3 +1 -32 -8 +2 -3 +27 +12 +38
    -17 +42 +27 +10 +5 -1 -1 +10 -17 +11 +18 +2 -19 -11 +18 +7 +23 -5 +21 -20 +2 -6 -20 -7 +16 -8 +41 +15 -3 -18 +16 +3 -2 +16 +8 -1 +3 +17 +21 +6 +19 +8 -14 +8 +4
    -1 +10 +7 -9 -20 -9 -60 +40 -14 -19 +38 -52 -13 -203 -31 -15 +1 -9 -12 +17 +10 -9 -5 -21 -5 -6 -11 +19 +10 -11 -16 -37 -22 -13 +5 +19 -14 -7 +13 -8 +26 +16 +19 -7 +28
    +16 -2 +18 +27 +13 -150 +5 +22 -6 -22 -14 -136 -91 -7 -14 +31 -278 -73081 +12 +15 -16 +6 -8 -3 +19 -3 +10 +1 +1 +8 +9 +9 -12 +9 -2 +14 +9 -19 +15 +21 +19 +1 +3 +19
    -11 +8 +20 -14 +16 +4 +6 -16 -3 -3 -13 -4 +5 +16 -5 -10 +3 -19 -5 +7 -16 -7 +10 +1 +18 +10 -12 -14 -15 -7 +14 +12 +16 +17 +11 +4 +12 +15 -17 +13 -8 +1 -12 -16 -10 -9
    -10 +8 -20 +8 -5 -7 -16 +9 -8 -13 -12 -8 +2 +3 +16 -15 +11 +11 +2 -3 -17 -17 -3 -7 -20 +18 -9 +3 -5 -10 -17 +16 -2 -19 -18 -12 -14 -17 -3 +6 +10 +16 +3 +2 -16 -16 -10
    -10 +14 -6 -10 +9 +15 +15 +7 -14 -2 +10 -14 -11 -2 +14 +16 +5 +20 +12 -18 +11 +9 +9 -3 -5 +12 +15 +6 -8 +3 +14 +15 -6 -12 -15 +23 -7 +18 -4 +18 +4 +9 +19 -7 +6 +3
    -10 +18 -19 -20 -6 +17 -15 +3 +20 -5 -10 -12 -23 +5 -1 -14 -16 -17 -12 +17 -14 +4 -12 +18 +20 -15 -19 -1 -15 +10 -9 +1 +3 -18 +19 -14 -19 +17 -11 -3 -13 +7 +19 -15
    +7 -33 -8 +2 +2 -18 -10 +16 -7 +4 -14 +8 +13 -5 +20 -14 +15 -11 -7 -22 -10 +11 +1 +16 -8 +16 -3 +15 +6 -17 +27 +14 +15 +8 +18 +21 -19 -25 +11 +10 +65 -11 -36 -15 -11 -25
    +18 +35 +72 +1 +58 +3 +12 +19 -10 +21 +16 +11 +9 +1 +1 +9 -6 +20 -12 -20 +5 +8 -7 +18 +19 -13 -15 -24 +8 -16 +3 +2 -14 -1 -10 -16 -17 +21 +4 +14 -17 +18 -12 +10 +11 +2
    -15 -4 -19 +13 +1 -18 -6 -23 -17 +19 +28 +6 +29 +10 +17 -6 +5 -11 +26 +25 -22 +2 -10 -29 +43 +17 +5 +4 +26 +1 +11 +19 -12 +20 +17 -13 +1 +19 +14 -19 -9 +2 +13 +4 -2
    +19 +10 -14 +10 -9 +1 +20 +16 +6 -13 +4 +19 +16 -6 -7 -25 -20 +5 +2 -3 -9 -21 -19 +12 -8 -7 +17 -15 -18 -11 +6 +3 +15 -5 -5 -6 -18 -5 +19 -5 +18 -1 +2 -16 -6 -16 +17 -8
    +16 +30 +18 +5 -2 +16 +19 -8 +9 -23 +12 +3 +18 +36 +50 -133 +7 +9 -68 +7 +2 -113 -85 -23 -211 -19 -6 -21 -11 -16 +19 +15 -13 -4 +14 +27 -12 -5 -18 -20 -16 -15 -15 -12 +1
    +6 +9 -11 +18 +5 -14 -19 -9 +18 +2 -18 -11 +3 +13 -4 -4 +9 -10 -17 -4 +16 +13 +19 -15 +6 -3 +4 +10 +20 +17 -24 -5 +1 +8 +27 +6 +4 +20 +8 -3 +66 -139 -21 +11 -19 +20 -13
    -31 +7 -2 +5 -2 +4 -16 +7 +6 -21 -10 -12 +25 -7 -17 -13 +73906'''

    lG = [int(x) for x in strIn.strip().split()]
    print lG, Sum(lG)

def Day1b():
    """Return the first resulting value that is hit twice by looping indefinitely through the input values"""

    strIn = '''
    -10 +18 +5 +1 +1 -19 -13 -4 -4 -5 -17 +13 -3 +18 -17 +14 +11 +14 +16 +6 -2 -3 -3 -5 +18 +17 -9 +14 +13 +3 -17 -3 +11 -4 -5 +3 +9 -20 -18 +10 +1 +1 -14
    +9 -5 +20 -6 +1 +2 +2 -13 -11 +18 +18 +1 +2 -11 +23 +2 -7 +2 +7 -3 +6 +9 +8 +13 -8 +12 +7 +4 +9 -11 -19 +1 +13 +15 -14 +10 +19 -6 +1 +7 -14 +3 +17 +2 +2
    +15 +15 +18 +6 -9 +8 +15 +12 +15 +5 +8 +1 +6 -13 +18 +10 +10 +7 +14 +4 +9 +17 +10 +6 +7 +9 +5 +1 +1 +19 +10 +18 -5 +10 +7 -6 -10 +17 -12 -15 -17 +5 +7 -11 +18
    -12 -12 -3 +10 -4 -5 +13 +10 -1 +7 -12 -11 -9 -18 +3 -1 -15 -7 -15 +4 -7 -4 -7 +19 -3 +14 +9 -11 -7 +16 -10 -3 +10 +13 +10 -7 +13 +11 +17 +7 +4 +20 +19 -1 -5
    +10 +7 -9 -14 -3 -15 +5 -19 +13 +9 -12 -6 -13 -15 -2 -15 -3 +11 +22 +19 +18 -6 +10 -9 +10 +19 -15 -2 +20 +12 -20 -8 +23 +15 -11 +10 -2 +8 -4 -19 +16 +16 -6 -22
    -2 +9 +13 -19 +8 +16 +18 +21 +17 +26 -19 +16 +8 -14 -1 +8 +9 +2 +6 +4 -7 -2 +1 +14 -3 +17 +6 +19 -14 +10 +13 -17 -10 +11 -14 -13 -13 +11 +19 +18 +1 -12 +14 -17 +8
    +11 +1 +15 +13 -12 +14 +2 -8 +9 +9 +2 +14 +7 +14 -1 -11 +13 -11 -3 -18 +7 -19 -1 -14 +4 -11 +12 -6 -19 +6 +15 -10 -9 +24 -9 -1 +14 +8 -5 -5 +12 +16 -14 +3 -6 +12
    +11 -18 +9 +17 +10 +11 -19 +13 +9 +4 +15 +8 -21 +5 -12 +4 +13 +13 +6 +1 +6 +4 +6 -14 -6 +17 -4 +10 +13 +17 +3 -5 +19 +6 -16 -8 +21 -19 +4 -15 -5 +7 -11 -19 +18 -2
    +10 -17 -8 -8 -10 +7 -19 -6 -11 +19 +5 +9 -11 +16 -13 -17 +5 -18 -1 +12 -9 -18 +25 -3 -8 -15 +9 -19 -5 +18 +5 +3 -1 -12 -12 +8 -21 +3 +1 -32 -8 +2 -3 +27 +12 +38
    -17 +42 +27 +10 +5 -1 -1 +10 -17 +11 +18 +2 -19 -11 +18 +7 +23 -5 +21 -20 +2 -6 -20 -7 +16 -8 +41 +15 -3 -18 +16 +3 -2 +16 +8 -1 +3 +17 +21 +6 +19 +8 -14 +8 +4
    -1 +10 +7 -9 -20 -9 -60 +40 -14 -19 +38 -52 -13 -203 -31 -15 +1 -9 -12 +17 +10 -9 -5 -21 -5 -6 -11 +19 +10 -11 -16 -37 -22 -13 +5 +19 -14 -7 +13 -8 +26 +16 +19 -7 +28
    +16 -2 +18 +27 +13 -150 +5 +22 -6 -22 -14 -136 -91 -7 -14 +31 -278 -73081 +12 +15 -16 +6 -8 -3 +19 -3 +10 +1 +1 +8 +9 +9 -12 +9 -2 +14 +9 -19 +15 +21 +19 +1 +3 +19
    -11 +8 +20 -14 +16 +4 +6 -16 -3 -3 -13 -4 +5 +16 -5 -10 +3 -19 -5 +7 -16 -7 +10 +1 +18 +10 -12 -14 -15 -7 +14 +12 +16 +17 +11 +4 +12 +15 -17 +13 -8 +1 -12 -16 -10 -9
    -10 +8 -20 +8 -5 -7 -16 +9 -8 -13 -12 -8 +2 +3 +16 -15 +11 +11 +2 -3 -17 -17 -3 -7 -20 +18 -9 +3 -5 -10 -17 +16 -2 -19 -18 -12 -14 -17 -3 +6 +10 +16 +3 +2 -16 -16 -10
    -10 +14 -6 -10 +9 +15 +15 +7 -14 -2 +10 -14 -11 -2 +14 +16 +5 +20 +12 -18 +11 +9 +9 -3 -5 +12 +15 +6 -8 +3 +14 +15 -6 -12 -15 +23 -7 +18 -4 +18 +4 +9 +19 -7 +6 +3
    -10 +18 -19 -20 -6 +17 -15 +3 +20 -5 -10 -12 -23 +5 -1 -14 -16 -17 -12 +17 -14 +4 -12 +18 +20 -15 -19 -1 -15 +10 -9 +1 +3 -18 +19 -14 -19 +17 -11 -3 -13 +7 +19 -15
    +7 -33 -8 +2 +2 -18 -10 +16 -7 +4 -14 +8 +13 -5 +20 -14 +15 -11 -7 -22 -10 +11 +1 +16 -8 +16 -3 +15 +6 -17 +27 +14 +15 +8 +18 +21 -19 -25 +11 +10 +65 -11 -36 -15 -11 -25
    +18 +35 +72 +1 +58 +3 +12 +19 -10 +21 +16 +11 +9 +1 +1 +9 -6 +20 -12 -20 +5 +8 -7 +18 +19 -13 -15 -24 +8 -16 +3 +2 -14 -1 -10 -16 -17 +21 +4 +14 -17 +18 -12 +10 +11 +2
    -15 -4 -19 +13 +1 -18 -6 -23 -17 +19 +28 +6 +29 +10 +17 -6 +5 -11 +26 +25 -22 +2 -10 -29 +43 +17 +5 +4 +26 +1 +11 +19 -12 +20 +17 -13 +1 +19 +14 -19 -9 +2 +13 +4 -2
    +19 +10 -14 +10 -9 +1 +20 +16 +6 -13 +4 +19 +16 -6 -7 -25 -20 +5 +2 -3 -9 -21 -19 +12 -8 -7 +17 -15 -18 -11 +6 +3 +15 -5 -5 -6 -18 -5 +19 -5 +18 -1 +2 -16 -6 -16 +17 -8
    +16 +30 +18 +5 -2 +16 +19 -8 +9 -23 +12 +3 +18 +36 +50 -133 +7 +9 -68 +7 +2 -113 -85 -23 -211 -19 -6 -21 -11 -16 +19 +15 -13 -4 +14 +27 -12 -5 -18 -20 -16 -15 -15 -12 +1
    +6 +9 -11 +18 +5 -14 -19 -9 +18 +2 -18 -11 +3 +13 -4 -4 +9 -10 -17 -4 +16 +13 +19 -15 +6 -3 +4 +10 +20 +17 -24 -5 +1 +8 +27 +6 +4 +20 +8 -3 +66 -139 -21 +11 -19 +20 -13
    -31 +7 -2 +5 -2 +4 -16 +7 +6 -21 -10 -12 +25 -7 -17 -13 +73906'''

    lN = [int(x) for x in strIn.strip().split()]

    setNFound = set()

    cN = len(lN)
    nT = 0
    i = 0
    while True:
        nT += lN[i % cN]
        i += 1
        if nT in setNFound:
            print nT, "found twice after", i, "sums"
            return

        setNFound.add(nT)

def Day2a():
    """Return C * D, where C = number of sequences that have a letter exactly twice, and D = number of sequences that have a letter
    exactly thrice. A sequence can bump any, none, or all of C and D."""

    cSeq2 = 0
    cSeq3 = 0

    for str0 in ain.s_strIn2.strip().split():
        mpChC = {}
        for ch in str0:
            c = mpChC.get(ch, 0)
            mpChC[ch] = c + 1

        setC = set(mpChC.values())
        if 2 in setC:
            cSeq2 += 1
        if 3 in setC:
            cSeq3 += 1

    print cSeq2, cSeq3, cSeq2 * cSeq3

def Day2b():
    """Return the common letters for the two sequences in ain.s_strIn2 which differ by exactly one character (i.e., find that pair, and return all but the mismatch letter)"""

    lSeq = ain.s_strIn2.strip().split()
    cSeq = len(lSeq)
    for i in range(cSeq):
        for j in range(cSeq):
            if i >= j:
                continue

            seq0 = lSeq[i]
            seq1 = lSeq[j]

            cCh = len(seq0)
            assert(len(seq1) == cCh)

            iChMiss = -1
            for k in range(cCh):
                if seq0[k] != seq1[k]:
                    if iChMiss != -1:
                        iChMiss = -1
                        break
                    else:
                        iChMiss = k

            if iChMiss != -1:
                print i, j, seq0, seq1, iChMiss, seq0[:iChMiss] + seq0[iChMiss+1:]

class Claim:
    def __init__(self, strIn):
        lPart = strIn.strip().split()
        self.m_id = lPart[0][1:]
        self.m_left = int(lPart[2].split(',')[0])
        self.m_top = int(lPart[2].split(',')[1][:-1])
        self.m_width = int(lPart[3].split('x')[0])
        self.m_height = int(lPart[3].split('x')[1])

def Day3a():
    """Fabric claims are #id @ L,D: WxH; find how many inches of the overall 1000x1000 space are multi-claimed"""

    lClaim = [Claim(x) for x in ain.s_strIn3.strip().split('\n')]
    print len(lClaim), 'claims'

    aaC = []
    for i in range(1000):
        aaC.append([0] * 1000)

    for claim in lClaim:
        x0 = claim.m_left
        x1 = x0 + claim.m_width
        y0 = claim.m_top
        y1 = y0 + claim.m_height

        y = y0
        while y < y1:
            x = x0
            while x < x1:
                aaC[y][x] += 1
                x += 1
            y += 1

    cOverlap = 0
    cHit = 0
    for y in range(1000):
        for x in range(1000):
            if aaC[y][x] > 1:
                cOverlap += 1
            elif aaC[y][x] > 0:
                cHit += 1

    print cHit, cOverlap

def Day3b():
    """Print the claim ID for the only claim that doesn't overlap with any other claims"""

    lClaim = [Claim(x) for x in ain.s_strIn3.strip().split('\n')]
    for claim0 in lClaim:
        x00 = claim0.m_left
        x01 = x00 + claim0.m_width
        y00 = claim0.m_top
        y01 = y00 + claim0.m_height

        fOverlap = False

        for claim1 in lClaim:
            if claim0 == claim1:
                continue

            x10 = claim1.m_left
            x11 = x10 + claim1.m_width
            y10 = claim1.m_top
            y11 = y10 + claim1.m_height

            # do bounding-box style (lack of) overlap detection

            if x01 < x10:
                continue    # no overlap
            if x11 < x00:
                continue    # no overlap
            if y01 < y10:
                continue    # no overlap
            if y11 < y00:
                continue    # no overlap

            # overlap
            fOverlap = True
            break

        if not fOverlap:
            print "Claim", claim0.m_id, "does not overlap any others"
            break


def LEvent4():
    """Read ain.s_strIn4 into events, sort them chronologically, and return the result"""

    s_reEv = re.compile(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)')
    lEvent = []
    for str0 in ain.s_strIn4.strip().split('\n'):
        match = s_reEv.search(str0)
        assert(match)

        lGr = match.groups()
        ts = (lGr[0], lGr[1], lGr[2], lGr[3], lGr[4])
        ev = lGr[5].split()[1]  # up, alseep, #NNNN
        lEvent.append((ts, ev))

    return sorted(lEvent)

def MpIdLr4():
    """Return mapping from guard ID to list of ranges where they're asleep"""

    lEvent = LEvent4()

    mpIdLr = {}
    lR = None
    pair = None
    for ev in lEvent:
        if ev[1].startswith('#'):
            lR = mpIdLr.setdefault(ev[1], [])
            pair = None
        elif ev[1] == 'up':
            assert(pair)
            assert(ev[0][3] == '00')
            pair.append(int(ev[0][4]))
            lR.append(pair)
            pair = None
        elif ev[1] == 'asleep':
            assert(pair == None)
            assert(ev[0][3] == '00')
            pair = [int(ev[0][4])]

    return mpIdLr

def Day4a():
    """Order entries chronologically; then, figure out which guard spends the most time asleep (G); then figure out which minute of the midnight hour they are asleep
    the most (M); then return their G.id * M"""

    mpIdLr = MpIdLr4()

    # find the guard who is asleep the most

    gidBest = None
    cBest = 0
    for gid, lR in mpIdLr.items():
        cGid = 0
        for r in lR:
            cGid += r[1] - r[0]

        if cGid > cBest:
            gidBest = gid
            cBest = cGid

    print gid, cBest

    # figure out which minute of the day they are asleep the most

    mpMinC = [0] * 60

    for r in mpIdLr[gidBest]:
        r0 = r[0]
        while r0 < r[1]:
            mpMinC[r0] += 1
            r0 += 1

    cBest = -1
    mBest = -1

    for m, c in enumerate(mpMinC):
        if c > cBest:
            mBest = m
            cBest = c

    # spit out the answer

    print mBest, int(gidBest[1:]) * mBest

def Day4b():
    """For all guards G, find overlapped sleep minutes M, and for maximal M, return M * G.id"""

    mpIdLr = MpIdLr4()

    gidBest = None
    cBest = 0
    mBest = 0
    for gid, lR in mpIdLr.items():
        mpMinC = [0] * 60

        cCur = -1
        mCur = -1
        for r in lR:
            r0 = r[0]
            while r0 < r[1]:
                mpMinC[r0] += 1

                if mpMinC[r0] > cCur:
                    cCur = mpMinC[r0]
                    mCur = r0

                r0 += 1

        if cCur > cBest:
            gidBest = gid
            cBest = cCur
            mBest = mCur

    print gidBest, cBest, mBest, mBest * int(gidBest[1:])


def StrCollapse(str0):
    """Given a "polymer" of letters, some upper, some lower, collapse nearby upper and lower letters of the same type by
    removing them. Run this process repeatedly until there is no further progress to be made, and spit out the result."""

    cRemove = 1
    while cRemove > 0:
        # print "pass removed {rem} pairs".format(rem=cRemove)
        cRemove = 0
        i = 0
        while i < len(str0) - 1:
            ch0 = str0[i]
            ch1 = str0[i+1]
            if ch0 != ch1 and ch0.lower() == ch1.lower():
                # found a pair to remove
                str1 = str0[:i] + str0[i+2:]
                assert(len(str1) == len(str0) - 2)
                str0 = str1
                cRemove += 1
                # NOTE (davidm) moving back by one here saves *tons* of runtime
                i = max(0, i - 1)
            else:
                i += 1

    return str0

def Day5a():
    """Given a "polymer" of letters, some upper, some lower, collapse nearby upper and lower letters of the same type by
    removing them. Run this process repeatedly until there is no further progress to be made, and spit out the result."""

    str0 = ain.s_strIn5.strip()

    str1 = StrCollapse(str0)

    print len(str0), len(str1)

def Day5b():
    """Figure out which letter pair (upper and lower the same character) when removed produces the shortest collapsed string"""

    str0 = ain.s_strIn5.strip()

    setCh = set(list(str0.lower()))
    print len(setCh), "characters possible to remove"

    cChBest = len(str0)
    for ch in setCh:
        str1 = str0.replace(ch, '')
        str1 = str1.replace(ch.upper(), '')
        str2 = StrCollapse(str1)

        print "remove {ch} gives {pre} and {post}".format(ch=ch, pre=len(str1), post=len(str2))

        if len(str2) < cChBest:
            cChBest = len(str2)

    print "Best (shortest) was {short}".format(short=cChBest)

def LPos6():
    """Convert the input for day 6 into a list of positions"""

    lPos = []
    for str0 in ain.s_strIn6.strip().split('\n'):
        x, y = [int(s.strip()) for s in str0.split(',')]
        lPos.append((x,y))

    return lPos

def SManh(pos0, pos1):
    """Return manhattan distance between two xy points"""

    return abs(pos0[0] - pos1[0]) + abs(pos0[1] - pos1[1])

def Day6a():
    """Calculate a manhattan distance field from a set of points where the field indicates which points are closest to one of the
    input coordinates. Using that map, determine which of the input points has the largest (finite) area. Bounds seem to be the
    square bounding area for all of the coordinates."""

    lPos = LPos6()

    print "Got {c} points to consider".format(c=len(lPos))

    # Calculate maximum side of the bounding box

    # BB (davidm) do I also need the minimum? question seems to start at 0,0
    # BB (davidm) hmm...question says largest finite, so I may have to discard those
    #  that are infinite (which I think means those that hit the edges of the area,
    #  because manhattan distance should always be closest to that, right?)

    posMax = [0,0]
    for pos in lPos:
        posMax[0] = max(posMax[0], pos[0] + 1)
        posMax[1] = max(posMax[1], pos[1] + 1)

    print "Bounds of area are {x} and {y}".format(x=posMax[0], y=posMax[1])

    assert(SManh((0, 0), (1, 1)) == SManh((1,1), (0,0)))
    assert(SManh((1,1), (2,2)) == 2)

    # Build a 2d grid to track which iPos is closest (manhattan) to any given point

    aIPosClosest = [-1] * (posMax[1] * posMax[0])

    mpIPosC = [0] * len(lPos)
    for y in range(posMax[1]):
        for x in range(posMax[0]):
            lS = [(SManh((x, y), lPos[i]), i) for i in range(len(lPos))]
            lS.sort()
            if lS[0][0] != lS[1][0]:
                # the top point is closest
                iPos = lS[0][1]
                aIPosClosest[y * posMax[0] + x] = iPos
                mpIPosC[iPos] += 1

    if True:
        # print out a text representation of what we calculated to see if it makes any kind of sense at all

        strKey = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'

        for y in range(posMax[1]):
            for x in range(posMax[0]):
                sys.stdout.write(strKey[aIPosClosest[y * posMax[0] + x]])
            sys.stdout.write('\n')

        for i, c in enumerate(mpIPosC):
            print i, c
    # calculate the set of position indices that are infinite (walk the edges)

    setIPosEdge = set()

    for x in range(posMax[0]):
        setIPosEdge.add(aIPosClosest[0 + x])
        setIPosEdge.add(aIPosClosest[posMax[0] * (posMax[1] - 1) + x])

    for y in range(posMax[1]):
        setIPosEdge.add(aIPosClosest[y * posMax[0] + 0])
        setIPosEdge.add(aIPosClosest[y * posMax[0] + posMax[0] - 1])

    print "Found {c} edge cells".format(c=len(setIPosEdge))

    # finally, calculate which iPos is has the largest number of cells, but doesn't hit an edge

    lC = [(c, i) for i, c in enumerate(mpIPosC)]
    lC.sort()

    while lC:
        c, iPos = lC[-1]
        lC = lC[:-1]

        if iPos not in setIPosEdge:
            print "Pos {i} is finite and hits {c} cells".format(i=iPos, c=c)
            break

def Day6b():
    """Calculate how many positions are in a region that's got a total distance (to all points) that is
    under 10000 units, manhattan"""

    lPos = LPos6()

    print "Got {c} points to consider".format(c=len(lPos))

    # Calculate maximum side of the bounding box

    posMax = [0,0]
    for pos in lPos:
        posMax[0] = max(posMax[0], pos[0] + 1)
        posMax[1] = max(posMax[1], pos[1] + 1)

    print "Bounds of area are {x} and {y}".format(x=posMax[0], y=posMax[1])

    assert(SManh((0, 0), (1, 1)) == SManh((1,1), (0,0)))
    assert(SManh((1,1), (2,2)) == 2)

    cPosUnder = 0

    for y in range(posMax[1]):
        for x in range(posMax[0]):
            lS = [SManh((x, y), pos) for pos in lPos]
            s = sum(lS)
            if s < 10000:
                cPosUnder += 1

    print "Found {c} positions in region of interest".format(c=cPosUnder)

if __name__ == '__main__':
    Day6b()
