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

def LPair7():
    """Return a list of pairs of the form (X,Y) meaning that X must happen before Y"""

    str0 = ain.s_strIn7

    lPair = []
    for str1 in str0.strip().split('\n'):
        lPart = str1.split()
        lPair.append((lPart[1], lPart[7]))

    return lPair

def Day7a():
    """Calculate the "ordering string" for the sequence of steps listed, all of the form X before Y, such that
    the alphabetically earliest of the available options is taken at each point until the whole graph is done."""

    lPair = LPair7()

    # convert pairs into a mapping from step to set of prereq steps; ensure that all listed steps are actually
    #  in the map for completeness

    mpStepSetPre = {}
    setStepAll = set()
    for step0, step1 in lPair:
        mpStepSetPre.setdefault(step1, set()).add(step0)
        mpStepSetPre.setdefault(step0, set())
        setStepAll.add(step0)
        setStepAll.add(step1)

    # loop calculating available (prereq met) steps and then marking alpha first complete

    setStepDone = set()
    lStepDone = []

    while setStepDone != setStepAll:
        # calculate available steps

        setStepAvail = set()
        for step, setPre in mpStepSetPre.items():
            if setPre & setStepDone == setPre and step not in setStepDone:
                setStepAvail.add(step)

        # mark a step complete

        lStep = sorted(setStepAvail)
        print "Available steps: {steps}".format(steps=str(lStep))

        lStepDone.append(lStep[0])
        setStepDone.add(lStep[0])

    print 'Final sequence:'
    print ''.join(lStepDone)

def Day7b():
    """So, using the same prereq logic as before, but assigning time cost and 5 workers, how long will it take before all is done?"""

    # NOTE (davidm) the order of completion may not be the same as before! Gah!
    # cost (in time) to complete step N = 60 + ord(N) - 65

    lPair = LPair7()

    # convert pairs into a mapping from step to set of prereq steps; ensure that all listed steps are actually
    #  in the map for completeness

    mpStepSetPre = {}
    setStepAll = set()
    for step0, step1 in lPair:
        mpStepSetPre.setdefault(step1, set()).add(step0)
        mpStepSetPre.setdefault(step0, set())
        setStepAll.add(step0)
        setStepAll.add(step1)

    # loop calculating available (prereq met) steps and then marking alpha first complete

    setStepDone = set()
    mpStepT = {}
    lStepDone = []
    tNow = 0

    while setStepDone != setStepAll:
        # calculate available steps

        setStepAvail = set()
        for step, setPre in mpStepSetPre.items():
            if setPre & setStepDone == setPre and step not in setStepDone:
                setStepAvail.add(step)

        # calculate what step(s) can be started; recall that we don't start steps
        #  that are currently running because they're currently running (got this wrong the first time!)

        lStep = sorted(setStepAvail - set(mpStepT.keys()))
        print "Available steps: {steps}".format(steps=str(lStep))

        cActive = len(mpStepT.keys())
        cStepNew = 5 - cActive
        lStep = lStep[:5]

        print "Starting steps {steps}".format(steps=str(lStep))

        # mark steps active

        for step in lStep:
            mpStepT[step] = tNow + 60 + ord(step) - 64

        # sort steps in order by when they end

        lTStep = [(t, step) for step, t in mpStepT.items()]
        lTStep.sort()

        # mark all steps that are done at the earliest time as done, and advance to that
        #  time

        tNow = lTStep[0][0]

        for t, step in lTStep:
            if t != tNow:
                break

            print "Marking {step} done at {t}".format(step=step, t=t)
            setStepDone.add(step)
            del(mpStepT[step])

        print "Ending time: {t}".format(t=tNow)

class Tree8:    # tag = t8
    def __init__(self):
        self.m_lT8Child = []
        self.m_lNData = []
        self.m_tcCache = None

    def Populate(self, strIn):
        """Given an encoded tree as input, assemble this tree as the root node, with child nodes underneath"""

        lN = [int(x) for x in strIn.strip().split()]

        self.Consume(lN)

    def Consume(self, lN):
        """Consume appropriate entries of lN, recursively building up a tree under this node"""

        # tree node: count of children, count of metadata, children, metadata

        assert(len(lN) >= 2)

        cChild = lN[0]
        cData = lN[1]

        # drop the first two elements from the list

        lN[0:2] = []

        assert(len(lN) >= cChild * 2 + cData)

        # pull children out of the list

        for iChild in range(cChild):
            self.m_lT8Child.append(Tree8())
            self.m_lT8Child[-1].Consume(lN)

        assert(len(lN) >= cData)
        self.m_lNData = lN[:cData]

        # drop the metadata from the list

        lN[0:cData] = []

    def TotalComplex(self):
        """Return the "total value" for this node, which is calculated via a complex set of constraints"""

        # if we've previously calculated this total, return its cached value

        if self.m_tcCache is not None:
            return self.m_tcCache

        # if a node has no children, its value is the sum of its metadata

        if not self.m_lT8Child:
            self.m_tcCache = sum(self.m_lNData)
            return self.m_tcCache

        # if a node has children, its metadata entries are child indices (1-indexed) which are to be added
        #  together. 0 = no child (skip), and entries outside of range otherwise are also skipped. Repeats
        #  are honored (1 1 = child0 * 2, for example).

        self.m_tcCache = 0
        for iChild1 in self.m_lNData:
            iChild0 = iChild1 - 1
            if iChild0 < 0:
                continue

            if iChild0 >= len(self.m_lT8Child):
                continue

            self.m_tcCache += self.m_lT8Child[iChild0].TotalComplex()

        return self.m_tcCache

def Day8a():
    """Given an encoded tree, assemble the tree, and then produce the sum of all of the metadata entries."""

    strIn = ain.s_strIn8
    t8 = Tree8()
    t8.Populate(strIn)

    total = 0
    lT8 = [t8]

    while lT8:
        t8 = lT8[0]
        lT8[0:1] = []
        total += sum(t8.m_lNData)
        lT8.extend(t8.m_lT8Child)

    print "Total is {tot}".format(tot=total)

def Day8b():
    """Calculate a more complex value; computation is in the Tree8 class."""

    strIn = ain.s_strIn8
    t8 = Tree8()
    t8.Populate(strIn)

    print "Total (complex) is {tot}".format(tot=t8.TotalComplex())

def Day9a():
    """Calculate something for N players on a wacky "marble game" listed in the rules"""

    strIn = "448 players; last marble is worth 71628 points"

    nMarbleMax = 71628 + 1
    cPlayer = 448

    mpIPlayerScore = {}

    lNCircle = [0]
    iNCur = 0
    iPlayer = 0
    nMarble = 1

    while nMarble < nMarbleMax:
        if nMarble % 23 == 0:
            # scoring round
            score = nMarble

            iNCur = (iNCur + len(lNCircle) - 7) % len(lNCircle)
            score += lNCircle[iNCur]
            lNCircle[iNCur:iNCur+1] = []

            mpIPlayerScore[iPlayer] = mpIPlayerScore.get(iPlayer, 0) + score

            #print "player {p} scored {t}, new total: {tot}".format(p=iPlayer, t=score, tot=mpIPlayerScore[iPlayer])
            #print lNCircle

        else:
            # standard insert round

            iNCur = (iNCur + 1) % len(lNCircle)
            iNCur += 1
            lNCircle[iNCur:iNCur] = [nMarble]
            #print lNCircle

        if nMarble % 10000 == 0:
            print "At marble {n}/{m} ({pct}%)".format(n=nMarble, m=nMarbleMax, pct=100.0 * nMarble / nMarbleMax)

        # advance marble and player

        nMarble += 1
        iPlayer = (iPlayer + 1) % cPlayer

    scoreBest = sorted(mpIPlayerScore.values())[-1]
    print "best score: {sc}".format(sc=scoreBest)

def Day9b():
    """Calculate something for N players on a wacky "marble game" listed in the rules"""

    strIn = "448 players; last marble is worth 7162800 points"

    # NOTE (davidm) this is...rather intractable to calculate via the same means as we did originally.
    # I'm guessing there's some formula that I can come up with to solve this, maybe? I'm going to try
    # spitting out the score numbers for a part of this to see what I can come up with instead.

    # well, I'm stumped for now. I'm not seeing a useful pattern anywhere, even with some interesting mods.
    # I can clearly figure out what half of the numbers that any given player picks up (they'll be the multiples
    # of 23 at iPlayer and then iPlayer + cPlayer, etc.). But the other half, I really don't see. I'm not detecting
    # what the appropriate sub-pattern is there. The "move back 7" thing, combined with the "move forward two" thing
    # ends up with my noodle being pretty thoroughly baked.

    # Couple further thoughts: the pattern of marbles that comes out is constant with respect to number of
    # players, so I shouldn't factor anything of particular note in there. If I can instead generate the
    # pattern of marbles coming out, I can then splatter that into the players to calculate the scores.

    # There is a surprising number of "plus 8" values in what I see. Unfortunately, that pattern is also irregular
    # so I'm currently unable to make much of it. Maybe that has something to do with the fact that we're going back
    # 7 values? Not super clear to me that's the case. The edit when the marble is removed, plus the 23 multiple that
    # never goes in, are both super crazy baking to my brain. I guess on the plus side, that means that every 23 marbles
    # we're actually minus two, not just one, so maybe there's a "mod 21" in there somewhere that makes all of this
    # stuff make sense? Hmm. I really feel like I'm just grasping at straws on this one.

    # I suppose I could also see if there's a better pattern in the "gained values" that we get out (the 23 + removed).
    # I tried looking at that, and once again, there are hopeful bits, but nothing that's directly jumping out at me as
    # the actual solution.

    # So, I'm going to investigate a different approach. I believe that I can (plus or minus) calculate what positional index
    # in the resulting list I should have for any given value, based on the highest value in the chain...maybe. The trick here
    # is that I'm not convinced (yet) that I can actually calculate that for sure, because I'm not certain which indices will
    # actually be removed as I'm calculating things. But what I *do* notice is that 0 is always at index 0 (unless maybe it gets
    # removed at some point), and (pre-23 removal) I have powers of two as the 1 index, with (obviously) all of the odd indices
    # progressing upwards one-at-a-time from that "anchor" value. The even indices, if we divide them by two, follow the same
    # pattern. The %23 removal step (with its additional removed value) throw all of that into a bit of disarray, unfortunately,
    # which is where things get tricky for me to understand.

    # maybe there *is* an N%M sum thing that I could come up with that makes the pattern of the totals and/or the extras?
    # or maybe the remove-7 number is something based on the 23 multiple that's removed?

    nMarbleMax = 7162800 + 1
    cPlayer = 448

    mpIPlayerScore = {}
    mpIPlayerLN = {}

    lNCircle = [0]
    iNCur = 0
    iPlayer = 0
    nMarble = 1

    lNRemoved = []
    lNRemoved2 = []

    while nMarble < nMarbleMax:
        if nMarble % 23 == 0:
            # scoring round
            score = nMarble
            lNRemoved2.append(score)

            mpIPlayerLN.setdefault(iPlayer, []).append(nMarble)

            iNCur = (iNCur + len(lNCircle) - 7) % len(lNCircle)
            score += lNCircle[iNCur]
            mpIPlayerLN[iPlayer].append(lNCircle[iNCur])
            lNRemoved.append(lNCircle[iNCur])
            lNRemoved2[-1] += lNCircle[iNCur]

            lNCircle[iNCur:iNCur+1] = []

            mpIPlayerScore[iPlayer] = mpIPlayerScore.get(iPlayer, 0) + score

            #print "player {p} scored {t}, new total: {tot}".format(p=iPlayer, t=score, tot=mpIPlayerScore[iPlayer])
            #print "  pieces: {ln}".format(ln=str(mpIPlayerLN[iPlayer]))
            #print "  pieces: {ln}".format(ln=str(sorted(mpIPlayerLN[iPlayer])))
            #print "  pieces mod  23: {ln}".format(ln=["{0:5n}".format(x % 23) for x in (mpIPlayerLN[iPlayer])])
            #print "  pieces mod 448: {ln}".format(ln=["{0:5n}".format(x % 448) for x in (mpIPlayerLN[iPlayer])])
            #print "  pieces mod   Z: {ln}".format(ln=["{0:5n}".format(x % (448 % 23)) for x in (mpIPlayerLN[iPlayer])])
            #print "  pieces mod   7: {ln}".format(ln=["{0:5n}".format(x % 7) for x in (mpIPlayerLN[iPlayer])])

            #print lNCircle

        else:
            # standard insert round

            iNCur = (iNCur + 1) % len(lNCircle)
            iNCur += 1
            lNCircle[iNCur:iNCur] = [nMarble]
            #print lNCircle

        if nMarble == 3000:
            print "At marble {n}/{m} ({pct}%)".format(n=nMarble, m=nMarbleMax, pct=100.0 * nMarble / nMarbleMax)
            print "Marbles removed (non-mod-23 ones): {ln}".format(ln=lNRemoved)
            print "Scores gained: {ln}".format(ln=lNRemoved2)
            print "Differences (n*23 - m7): {ln}".format(ln=[23 * (i+1) - n for i, n in enumerate(lNRemoved)])
            break

        # advance marble and player

        nMarble += 1
        iPlayer = (iPlayer + 1) % cPlayer

    scoreBest = sorted(mpIPlayerScore.values())[-1]
    print "best score: {sc}".format(sc=scoreBest)

    pass

def LPvDay10():
    """Return a list of 4-tuples like (x, y, dx, dy) for the program input"""

    rePv = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>')

    lPv = []
    for str0 in ain.s_strIn10.strip().split('\n'):
        match = rePv.search(str0)
        if not match:
            continue

        lStr = match.groups()
        lPv.append(tuple([int(x) for x in lStr]))
        assert(len(lPv[-1]) == 4)

    return lPv

def IncrementLPv(lPv, dT):
    """Increment (or decrement with dT -1) lPv coordinates based on their (dx,dy) values in place"""

    for i in range(len(lPv)):
        pv = lPv[i]
        lPv[i] = (pv[0] + dT * pv[2], pv[1] + dT * pv[3], pv[2], pv[3])

def DrawLPv(lPv):
    """Display (somehow) the given lPv values"""

    # calculate display limits

    lX = [pv[0] for pv in lPv]
    lX.sort()
    x0 = lX[0]
    x1 = lX[-1] + 1

    lY = [pv[1] for pv in lPv]
    lY.sort()
    y0 = lY[0]
    y1 = lY[-1] + 1

    # calculate set of positions

    setP = set([(pv[0], pv[1]) for pv in lPv])

    # draw stuff by checking the set

    print "----"
    y = y0
    while y < y1:
        x = x0
        while x < x1:
            ch = '.'
            if (x, y) in setP:
                ch = '#'
            sys.stdout.write(ch)
            x += 1
        sys.stdout.write('\n')
        y += 1

def Day10a():
    """Given starting points and velocities (all in 2-d, left->right, top->bottom coordinates), calculate forward step by step to figure
    out what the message will be when all of the points are properly coincident to form letters."""

    # basic idea 1: just plot pictographically each time, and allow me to scan through them until I see something. Not great, but
    #  might be doable.

    # basic idea 2: like idea 1, roughly, but keep track of the "smallest" approach that I get on the various values, and center the
    #  acutal message search on times near that figuring that points will otherwise be mostly more divergent. Seems like this might be
    #  worth pursuing, since I'm not sure the extents or time deltas necessary to look through the actual input data.

    lPv = LPvDay10()

    lX = [pv[0] for pv in lPv]
    lY = [pv[1] for pv in lPv]
    posMax = (max(lX), max(lY))
    posMin = (min(lX), min(lY))

    cIter = 0
    while True:
        # advance the positions forwards in time

        cIter += 1
        IncrementLPv(lPv, 1)

        lX = [pv[0] for pv in lPv]
        lY = [pv[1] for pv in lPv]
        posMaxCur = (max(lX), max(lY))
        posMinCur = (min(lX), min(lY))

        if posMaxCur[0] >= posMax[0] and posMaxCur[1] >= posMax[1]:
            # maximum increasing, so probably diverging again
            break

        if posMinCur[0] <= posMin[0] and posMinCur[1] <= posMin[1]:
            # minimum decreasing, so probably diverging again
            break

        # update best max/min values

        posMax = (min(posMax[0], posMaxCur[0]), min(posMax[1], posMaxCur[1]))
        posMin = (max(posMin[0], posMinCur[0]), max(posMin[1], posMinCur[1]))

    # show some stuff, in hopes that it all makes sense somewhere

    print "Saw divergence start at iteration {i}, replaying some previous in hopes they work:".format(i=cIter)

    for i in range(5):
        DrawLPv(lPv)
        IncrementLPv(lPv, -1)

def Day10b():
    pass

if __name__ == '__main__':
    Day10a()
    Day10b()
