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

            if nMarble < 1000:
                print "player {p} scored {t}, new total: {tot}".format(p=iPlayer, t=score, tot=mpIPlayerScore[iPlayer])

            #print "player {p} scored {t}, new total: {tot}".format(p=iPlayer, t=score, tot=mpIPlayerScore[iPlayer])
            #print lNCircle

        else:
            # standard insert round

            iNCur = (iNCur + 1) % len(lNCircle)
            iNCur += 1
            lNCircle[iNCur:iNCur] = [nMarble]
            #print lNCircle

        #if nMarble % 10000 == 0:
            #print "At marble {n}/{m} ({pct}%)".format(n=nMarble, m=nMarbleMax, pct=100.0 * nMarble / nMarbleMax)

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

    # ok, totally different thought: perhaps the issue here is that I'm just doing things naively with a list, which means that
    #  every insert is pushing around a whole bunch of elements. perhaps all that I need to make things run in a tenable amount
    #  of time is to *actually* use a doubly-linked list, so that elements are just hanging out. we'll make millions of them, but
    #  that's fine, and the key is that we'll only visit things as we need to, not shuffle everything around whenever anything
    #  changes. I'm going to give that a whirl and see if that works better. Hopefully it will. :)

    nMarbleMax = 7162800 + 1
    cPlayer = 448

    class Marble:
        def __init__(self, n):
            self.m_n = n
            self.m_prev = None
            self.m_next = None

    mpIPlayerScore = {}

    # initialize "circle" that's all just itself

    marbleCur = Marble(0)
    marbleCur.m_prev = marbleCur
    marbleCur.m_next = marbleCur
    marble0 = marbleCur

    iNCur = 0
    iPlayer = 0
    nMarble = 1

    lNRemoved = []

    while nMarble < nMarbleMax:
        if nMarble % 23 == 0:
            # scoring round
            score = nMarble

            # find the 7th previous marble

            for i in range(7):
                marbleCur = marbleCur.m_prev

            # update the score

            score += marbleCur.m_n
            mpIPlayerScore[iPlayer] = mpIPlayerScore.get(iPlayer, 0) + score

            # remove the marble we're dropping

            marbleDel = marbleCur
            marbleCur = marbleCur.m_next
            marbleDel.m_prev.m_next = marbleDel.m_next
            marbleCur.m_prev = marbleDel.m_prev

            #if nMarble < 1000:
                #print "player {p} scored {t}, new total: {tot}".format(p=iPlayer, t=score, tot=mpIPlayerScore[iPlayer])

            #print lNCircle

        else:
            # standard insert round

            marbleCur = marbleCur.m_next
            marbleNew = Marble(nMarble)

            # do the pointer shuffling for the insert

            marbleNew.m_prev = marbleCur
            marbleNew.m_next = marbleCur.m_next
            marbleCur.m_next = marbleNew
            marbleNew.m_next.m_prev = marbleNew
            marbleCur = marbleNew

        if nMarble % 100000 == 0:
            print "At marble {mC} of {mM} ({pct:.2f}%)".format(mC=nMarble, mM=nMarbleMax, pct=100.0*nMarble/nMarbleMax)

        # advance marble and player

        nMarble += 1
        iPlayer = (iPlayer + 1) % cPlayer

    scoreBest = sorted(mpIPlayerScore.values())[-1]
    print "best score: {sc}".format(sc=scoreBest)

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

def Day11a():
    """Return the upper left coordinate of the 1-indexed 3x3 subgrid of a grid of 300x300 cells which has the highest sum"""

    # my personal input

    serial = 3031

    # construct the power grid

    mpX1Y1 = {}
    for x0 in range(300):
        x1 = x0 + 1
        mpX1Y1[x1] = {}
        for y0 in range(300):
            y1 = y0 + 1

            rackId = x1 + 10
            power = rackId * y1
            power += serial
            power *= rackId
            digit = (power / 100) % 10 if power > 100 else 0
            power = digit - 5

            mpX1Y1[x1][y1] = power

    # scan 3x3 subgrids to find the one with the highest total

    powerBest = -100000 # hopefully small enough
    cornerBest = (-1,-1)

    for x0 in range(300 - 3):
        x1 = x0 + 1
        for y0 in range(300 - 3):
            y1 = y0 + 1

            corner = (x1, y1)
            power = 0
            for dX in range(3):
                for dY in range(3):
                    power += mpX1Y1[x1 + dX][y1 + dY]

            if power > powerBest:
                cornerBest = corner
                powerBest = power

    print "Best corner is at ({x},{y}) with power {p}".format(x=cornerBest[0], y=cornerBest[1], p=powerBest)

def Day11b():
    """Using the mapping from part a, calculate the best square subgrid of any size (x,y,size)"""

    # my personal input

    serial = 3031

    # construct the power grid

    mpX1Y1 = {}
    for x0 in range(300):
        x1 = x0 + 1
        mpX1Y1[x1] = {}
        for y0 in range(300):
            y1 = y0 + 1

            rackId = x1 + 10
            power = rackId * y1
            power += serial
            power *= rackId
            digit = (power / 100) % 10 if power > 100 else 0
            power = digit - 5

            mpX1Y1[x1][y1] = power

    # scan all square subgrids to find the one with the highest total

    powerBest = -100000 # hopefully small enough
    sizeBest = -1
    cornerBest = (-1,-1)

    for x0 in range(300):
        x1 = x0 + 1
        print "Scanning x1 at {x1}".format(x1=x1)

        for y0 in range(300):
            y1 = y0 + 1

            corner = (x1, y1)

            # calculate consecutively larger sizes starting at this corner, tracking
            #  the power total for each square subgrid as we get it

            # NOTE (davidm) by doing this, we avoid an extra multiplier on the time to
            #  calculate an answer by avoiding recalculating all of the "smaller" squares
            #  anytime we want to calculate a "larger" square with the same origin corner

            power = 0
            size = 1
            while max(x1, y1) + size < 301:
                for dX in range(size):
                    power += mpX1Y1[x1 + dX][y1 + size - 1]
                for dY in range(size - 1):
                    power += mpX1Y1[x1 + size - 1][y1 + dY]

                if power > powerBest:
                    cornerBest = corner
                    powerBest = power
                    sizeBest = size
                    print "  Best so far: ({x},{y},{s}) with {p}".format(x=x1, y=y1, s=size, p=power)

                size += 1

    print "Best corner is at ({x},{y},{size}) with power {p}".format(x=cornerBest[0], y=cornerBest[1], p=powerBest, size=sizeBest)

def SetIPlant12():
    """Return a set of indices that have plants for the inital state of day 12"""

    strInit = ain.s_strIn12.strip().split('\n')[0]
    lPart = strInit.split()
    assert len(lPart) == 3

    pattern =  lPart[-1]

    setIPlant = set()
    for i, ch in enumerate(pattern):
        if ch == '#':
            setIPlant.add(i)
        else:
            assert ch == '.'

    return setIPlant

class Rule12:
    def __init__(self, strIn):
        self.m_setDIPlant = set()
        self.m_plant = None

        # parse strIn into a set of delta indices that have plants and the result

        lPart = strIn.split()
        assert len(lPart) == 3
        assert len(lPart[0]) == 5
        assert len(lPart[-1]) == 1

        for i, ch in enumerate(lPart[0]):
            if ch == '#':
                self.m_setDIPlant.add(i - 2)

        self.m_plant = True if lPart[-1] == '#' else False

    def Match(self, setIPlant, i):
        for di in [-2, -1, 0, 1, 2]:
            fSetPlant = (i + di) in setIPlant
            fSetRule = di in self.m_setDIPlant

            if fSetPlant != fSetRule:
                return False

        return True

def LRule12():
    """Return set of rules for day 12 puzzle"""

    lStr = ain.s_strIn12.strip().split('\n')
    assert lStr[0].startswith('initial')
    assert lStr[1] == ''

    lRule = []
    for str0 in lStr[2:]:
        lRule.append(Rule12(str0))

    return lRule

def Day12a():
    # input is #.#..# where # = occupied, . = empty, and the first is element 0, moving positively as we go. Note that there are also
    #  negative pots, which are all starting off empty.

    # also have "rules" of the form LLCRR => [.#] meaning that if the pattern looks like LLCRR, C will then have . or # as listed

    # want to figure what happens after 20 generations

    # want to sum up all pot numbers containing plants at gen 20, with initial state being gen 0

    setIPlant0 = SetIPlant12()
    lRule = LRule12()

    setIPlantPrev = setIPlant0

    iGen = 0
    while iGen < 20:
        iGen += 1

        # for each position of interest (current max/min plant plus slop) check for applicable rule and
        #  update next generation set as appropriate

        iMic = min(setIPlantPrev) - 6
        iMac = max(setIPlantPrev) + 6

        setIPlantNext = set()
        for di in range(iMac - iMic):
            i = iMic + di

            for rule in lRule:
                if rule.Match(setIPlantPrev, i):
                    if rule.m_plant:
                        setIPlantNext.add(i)
                    break

        print sorted(setIPlantNext)
        setIPlantPrev = setIPlantNext

    print "Total: {s}".format(s=sum(setIPlantNext))

def Day12b():
    # input is #.#..# where # = occupied, . = empty, and the first is element 0, moving positively as we go. Note that there are also
    #  negative pots, which are all starting off empty.

    # also have "rules" of the form LLCRR => [.#] meaning that if the pattern looks like LLCRR, C will then have . or # as listed

    # want to figure what happens after 20 generations

    # want to sum up all pot numbers containing plants at gen 20, with initial state being gen 0

    setIPlant0 = SetIPlant12()
    lRule = LRule12()

    setIPlantPrev = setIPlant0

    iGen = 0
    cGen = 50000000000
    fIdentical = False
    while iGen < cGen:
        iGen += 1

        # for each position of interest (current max/min plant plus slop) check for applicable rule and
        #  update next generation set as appropriate

        iMic = min(setIPlantPrev) - 6
        iMac = max(setIPlantPrev) + 6

        setIPlantNext = set()
        for di in range(iMac - iMic):
            i = iMic + di

            for rule in lRule:
                if rule.Match(setIPlantPrev, i):
                    if rule.m_plant:
                        setIPlantNext.add(i)
                    break

        # check for steady-state, where we're just generating an offset version of the same pattern over and over

        setIPlantNext0 = set()
        for i in setIPlantPrev:
            setIPlantNext0.add(i+1)

        if setIPlantNext0 == setIPlantNext:
            if not fIdentical:
                fIdentical = True
            else:
                print "At iGen {i} hit double pattern repeat: {pat}".format(i=iGen, pat=str(sorted(setIPlantNext)))
                break
        else:
            fIdentical = False

        setIPlantPrev = setIPlantNext

    # convert identical pattern at a generation to the cGen version

    setDi = set()
    for i in setIPlantNext:
        setDi.add(i - iGen)

    setIPlantEnd = set()
    for di in setDi:
        setIPlantEnd.add(di + cGen)

    print "Result: {pat}".format(pat=str(sorted(setIPlantEnd)))
    print "Total: {s}".format(s=sum(setIPlantEnd))

    pass

class Cart13:
    """Represents a cart on a track"""

    s_lTurn = ['left', 'straight', 'right']

    def __init__(self, x, y, dx, dy):
        self.m_x = x
        self.m_y = y
        self.m_dx = dx
        self.m_dy = dy
        self.m_iTurn = 0
        self.m_tick = None

    def PosNext(self):
        return (self.m_x + self.m_dx, self.m_y + self.m_dy)

    def UpdatePos(self, posNext, trackNext, tick):
        if trackNext == '-':
            assert self.m_dy == 0
            assert self.m_dx != 0
        elif trackNext == '|':
            assert self.m_dy != 0
            assert self.m_dx == 0
        elif trackNext == '/':
            self.m_dx, self.m_dy = -self.m_dy, -self.m_dx
        elif trackNext == '\\':
            self.m_dx, self.m_dy = self.m_dy, self.m_dx
        elif trackNext == '+':
            turn = Cart13.s_lTurn[self.m_iTurn]

            if turn == 'left':
                self.m_dx, self.m_dy = self.m_dy, -self.m_dx
            elif turn == 'straight':
                pass    # no change in direction
            elif turn == 'right':
                self.m_dx, self.m_dy = -self.m_dy, self.m_dx

            self.m_iTurn = (self.m_iTurn + 1) % len(Cart13.s_lTurn)
        else:
            assert False, "Bad track in cart advance"

        self.m_x, self.m_y = posNext
        self.m_tick = tick
        assert (self.m_dx == 0) != (self.m_dy == 0)

class Course13:
    """Represents a course (track + carts)"""

    def __init__(self, strIn):
        self.m_dX = 0
        self.m_dY = 0
        self.m_mpXYTrack = {}
        self.m_lCart = []
        self.m_xCol = None
        self.m_yCol = None
        self.m_fClear = False

        self.Parse(strIn)

    def SetClearCollisions(self, fClear):
        self.m_fClear = fClear

    def Parse(self, strIn):
        lStr = strIn.split('\n')
        if lStr[0] == '':
            lStr = lStr[1:]
        self.m_dY = len(lStr)
        self.m_dX = max([len(str0) for str0 in lStr])

        for y, str0 in enumerate(lStr):
            for x, ch in enumerate(str0):
                if ch in set(['-', '|', '\\', '/', '+']):
                    self.m_mpXYTrack[(x,y)] = ch
                elif ch == '<':
                    self.m_mpXYTrack[(x,y)] = '-'
                    self.m_lCart.append(Cart13(x, y, -1, 0))
                elif ch == '>':
                    self.m_mpXYTrack[(x,y)] = '-'
                    self.m_lCart.append(Cart13(x, y, 1, 0))
                elif ch == '^':
                    self.m_mpXYTrack[(x,y)] = '|'
                    self.m_lCart.append(Cart13(x, y, 0, -1))
                elif ch == 'v' or ch == 'V':
                    self.m_mpXYTrack[(x,y)] = '|'
                    self.m_lCart.append(Cart13(x, y, 0, 1))

    def Advance(self, tick):
        """Run the carts all forward one step, checking for collisions"""

        mpPosCart = {}
        for cart in self.m_lCart:
            mpPosCart[(cart.m_x, cart.m_y)] = cart

        for y in range(self.m_dY):
            for x in range(self.m_dX):
                posPrev = (x,y)

                cart = mpPosCart.get(posPrev, None)
                if not cart:
                    continue

                if cart.m_tick == tick:
                    # already handled this cart this tick
                    continue

                posNext = cart.PosNext()

                cartOther = mpPosCart.get(posNext, None)

                if cartOther:
                    # found a collision
                    if not self.m_fClear:
                        self.m_xCol = posNext[0]
                        self.m_yCol = posNext[1]
                        return
                    else:
                        # remove the collided carts

                        del mpPosCart[posNext]
                        del mpPosCart[posPrev]
                        continue

                # didn't hit anything

                cart.UpdatePos(posNext, self.m_mpXYTrack[posNext], tick)

                # update the cart position map

                del mpPosCart[posPrev]
                mpPosCart[posNext] = cart

        if self.m_fClear:
            # update the list of carts to be just those we're still tracking

            self.m_lCart = mpPosCart.values()

    def FHasCollision(self):
        return self.m_xCol is not None

    def XCol(self):
        return self.m_xCol

    def YCol(self):
        return self.m_yCol

    def Print(self):
        mpXYCart = {}
        for cart in self.m_lCart:
            mpXYCart[(cart.m_x, cart.m_y)] = cart

        for y in range(self.m_dY):
            for x in range(self.m_dX):
                cart = mpXYCart.get((x,y), None)
                if cart:
                    ch = '<'
                    if cart.m_dx == 1:
                        ch = '>'
                    elif cart.m_dy == -1:
                        ch = '^'
                    elif cart.m_dy == 1:
                        ch = 'v'
                    sys.stdout.write(ch)
                else:
                    sys.stdout.write(self.m_mpXYTrack.get((x,y), ' '))
            sys.stdout.write('\n')

def Day13a():
    """Run a little "minecart" simulation to determine where the first intersection occurs"""

    # valid track areas: | - / \ +
    # valid carts: > < ^ v
    # carts turn L, S, R (repeat) at intersections, per cart
    # carts solve top to bottom, left to right within a row

    course = Course13(ain.s_strIn13)

    tick = 0
    while True:
        tick += 1
        #print "Running tick {tick}".format(tick=tick)
        course.Advance(tick)
        #course.Print()
        if course.FHasCollision():
            break

    print "Collision at tick {tick} and pos ({x},{y})".format(tick=tick, x=course.XCol(), y=course.YCol())

def Day13b():
    """Run the "minecart" simulation, removing all colliding carts as they hit, and then determine the location of the final remaining cart"""

    course = Course13(ain.s_strIn13)
    course.SetClearCollisions(True)

    tick = 0
    while True:
        tick += 1
        cCart0 = len(course.m_lCart)
        #print "Running tick {tick}".format(tick=tick)
        course.Advance(tick)
        cCart1 = len(course.m_lCart)

        if cCart1 < 2:
            break
        elif cCart0 != cCart1:
            print "Removed {c} carts at tick {t}; {r} remain".format(c=cCart0 - cCart1, t=tick, r=cCart1)

    cart = course.m_lCart[0]
    print "Last cart at tick {tick} and pos ({x},{y})".format(tick=tick, x=cart.m_x, y=cart.m_y)

def Day14a():
    """Calculate what the 10 recipes following my target number are (each recipe is a single digit). Recipes combine by adding together and appending
    the individual digits of the result to the recipe list."""

    # pre-allocate a big array to hold everything so that we can minimize copies (thanks python)

    iGoal = 598701  # from my puzzle input

    lN = [-1] * (iGoal + 12)

    # initialize to proper starting state

    iWrite = 2
    iCook0 = 0
    iCook1 = 1
    lN[0] = 3
    lN[1] = 7

    while iWrite < iGoal + 10:
        # Fill in next recipe score

        iWritePrev = iWrite

        scoreNext = lN[iCook0] + lN[iCook1]
        if scoreNext > 9:
            # two digits
            lN[iWrite] = 1
            iWrite += 1
            lN[iWrite] = scoreNext - 10
            iWrite += 1
        else:
            # one digit
            lN[iWrite] = scoreNext
            iWrite += 1

        # advance the cooks

        step0 = lN[iCook0] + 1
        step1 = lN[iCook1] + 1

        iCook0 = (iCook0 + step0) % iWrite
        iCook1 = (iCook1 + step1) % iWrite

        # show some basic stuff

        if iWrite < 20:
            print lN[:iWrite + 1]

        # show some progress (to verify that we're proceeding ok)

        if iWritePrev / 1000 != iWrite / 1000:
            print "Writing at {i} ({pct:.2f}%)".format(i=iWrite, pct=100.0 * iWrite / (iGoal + 10))

    print 'Last recipes:'
    print ''.join([str(n) for n in lN[iGoal:iGoal + 10]])

def Day14b():
    """Calculate new recipes until we find the goal sequence in the recipe sequence, and then report how many recipes preceed that"""

    # pre-allocate a big array to hold everything so that we can minimize copies (thanks python)

    iGoal = 598701  # from my puzzle input
    lNGoal = [int(n) for n in list(str(iGoal))]

    # NOTE (davidm) I started at 5x, and then just doubled each time I couldn't find what I was looking for, until I got to 40.
    #  Luckily this doesn't take that long to run. A better version, perhaps, would be to either just trust python to do the right
    #  thing with a growing list, or to include new list allocations directly (alloc new, then copy), so that the size wouldn't
    #  have to be specified.

    lN = [-1] * (40 * iGoal)     # total guess, hopefully we'll find it...

    # initialize to proper starting state

    iWrite = 2
    iCook0 = 0
    iCook1 = 1
    lN[0] = 3
    lN[1] = 7
    iGoal = None

    while iWrite < len(lN) - 2:
        # Fill in next recipe score

        iWritePrev = iWrite

        scoreNext = lN[iCook0] + lN[iCook1]
        if scoreNext > 9:
            # two digits
            lN[iWrite] = 1
            iWrite += 1
            lN[iWrite] = scoreNext - 10
            iWrite += 1
        else:
            # one digit
            lN[iWrite] = scoreNext
            iWrite += 1

        # advance the cooks

        step0 = lN[iCook0] + 1
        step1 = lN[iCook1] + 1

        iCook0 = (iCook0 + step0) % iWrite
        iCook1 = (iCook1 + step1) % iWrite

        # check the last recipes in sequence to see if they're the goal

        if len(lN) > len(lNGoal):
            # check the second-to-last set (could have added two digits)

            if lN[iWrite - len(lNGoal) - 1:iWrite - 1] == lNGoal:
                # found the first occurrence of the sequence
                iGoal = iWrite - len(lNGoal) - 1
                break

            # check the last set (we could have added two digits)

            if lN[iWrite - len(lNGoal):iWrite] == lNGoal:
                # found the first occurrence of the sequence
                iGoal = iWrite - len(lNGoal)
                break

        # show some progress (to verify that we're proceeding ok)

        if iWritePrev / 1000 != iWrite / 1000:
            print "Writing at {i} ({pct:.2f}%)".format(i=iWrite, pct=100.0 * iWrite / len(lN))
            print "Compared {l0} to {l1} for example".format(l0=lN[iWrite - len(lNGoal):iWrite], l1=lNGoal)

    if iGoal is not None:
        print 'Goal found starting at {i}'.format(i=iGoal)
    else:
        print 'Did not find goal :('

class Entity15: # tag = entity
    """Entity in an arena; can be wall, floor, goblin, or elf"""

    setEtype = set(['#', '.', 'G', 'E'])

    # NOTE (davidm) ldPos is in "reading" order -- up, then left, then right, then down

    ldPos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    def __init__(self, pos, etype, arena):
        self.m_etype = etype
        self.m_pos = pos
        self.m_hp = 200     # not applicable for walls, floors
        self.m_dHp = 3      # damage done, not applicable for walls, floors
        self.m_arena = arena

        assert etype in Entity15.setEtype

    def MpPosPrevCompute(self):
        """Calculate all places that can be reached by this entity; resulting map has tuples at each pos with (cost, y, x, dy0, dx0)"""

        lPrev = [(0, self.m_pos[1] + dy, self.m_pos[0] + dx, dy, dx) for dx, dy in Entity15.ldPos]

        mpPosPrev = {}
        while lPrev:
            prev = lPrev[0]
            lPrev = lPrev[1:]

            entity = self.m_arena.m_mpPosEntity.get((prev[2], prev[1]), None)
            if not entity or entity.m_etype != '.':
                # blocked/illegal, so skip
                continue

            if mpPosPrev.get((prev[2], prev[1]), None) != None:
                # already found this position, so don't keep it again with a worse score
                continue

            # mark how we got to this position (steps, direction taken)

            mpPosPrev[(prev[2], prev[1])] = prev

            # add new explore locations to check from here

            lPrev.extend([(prev[0] + 1, prev[1] + dy, prev[2] + dx, prev[3], prev[4]) for dx, dy in Entity15.ldPos])

        return mpPosPrev

    def Move(self, lEntityT):
        """Calculate the desired move for this entity"""

        # Determine possible desired ending locations (open spaces by targets)

        lPosDest = []
        for entity in lEntityT:
            lPosTry = [(entity.m_pos[0] + dx, entity.m_pos[1] + dy) for dx, dy in Entity15.ldPos]
            for pos in lPosTry:
                entity = self.m_arena.m_mpPosEntity.get(pos, None)
                if entity and entity.m_etype == '.':
                    lPosDest.append(pos)

        if not lPosDest:
            # cannot move, so give up
            return

        # Calculate BFS flood-filled reachability map for this entity

        mpPosPrev = self.MpPosPrevCompute()

        # Find best target (shortest distance, tiebreak with reading order of destination, with initial direction
        #  always chosen reading order when multiple exist)

        prevBest = None
        for pos in lPosDest:
            prev = mpPosPrev.get(pos, None)
            if prev == None:
                continue

            if not prevBest:
                prevBest = prev
            else:
                prevBest = min(prevBest, prev)

        if not prevBest:
            # nothing could be reached, so give up
            return

        # move to the desired space

        dy, dx = prevBest[3:]
        self.m_arena.m_mpPosEntity[self.m_pos] = Entity15(self.m_pos, '.', self.m_arena)
        self.m_pos = (self.m_pos[0] + dx, self.m_pos[1] + dy)
        entityDest = self.m_arena.m_mpPosEntity.get(self.m_pos, None)
        assert entityDest
        assert entityDest.m_etype == '.'
        self.m_arena.m_mpPosEntity[self.m_pos] = self

    def Advance(self):
        """Advance this unit one round"""

        # identify targets and do nothing if there aren't any

        lEntityT = self.m_arena.LElf() if self.m_etype == 'G' else self.m_arena.LGoblin()

        if not lEntityT:
            print "Ran out of opponents!"
            self.m_arena.m_fEndCombat = True
            return

        # Check if a target is already in range

        fMove = True
        etypeT = 'G' if self.m_etype == 'E' else 'E'

        for dx, dy in Entity15.ldPos:
            entityT = self.m_arena.m_mpPosEntity.get((self.m_pos[0] + dx, self.m_pos[1] + dy), None)
            if entityT is not None and entityT.m_etype == etypeT:
                fMove = False
                break

        if fMove:
            # no in-range target, so try to move

            self.Move(lEntityT)

        # Check if we can attack something

        targBest = None
        for dx, dy in Entity15.ldPos:
            entityT = self.m_arena.m_mpPosEntity.get((self.m_pos[0] + dx, self.m_pos[1] + dy), None)
            if entityT is None or entityT.m_etype != etypeT:
                continue

            targ = (entityT.m_hp, entityT.m_pos[1], entityT.m_pos[0], entityT)
            if not targBest:
                targBest = targ
            else:
                targBest = min(targBest, targ)

        if not targBest:
            # no target, so no attack
            return

        # Attack the target

        entityT = targBest[3]
        entityT.m_hp -= self.m_dHp
        if entityT.m_hp < 1:
            # target died, so replace them with a floor space

            self.m_arena.m_mpPosEntity[entityT.m_pos] = Entity15(entityT.m_pos, '.', self.m_arena)

class Arena15:  # tag = arena
    """Arena of walls, floors, and units"""

    def __init__(self, strIn):
        self.m_mpPosEntity = {}
        self.m_iRound = 0
        self.m_fEndCombat = False

        # load data from strIn regarding the arena

        for y, str0 in enumerate(strIn.strip().split('\n')):
            for x, ch in enumerate(str0):
                assert not self.m_mpPosEntity.has_key((x,y))
                self.m_mpPosEntity[(x,y)] = Entity15((x,y), ch, self)

    def Advance(self):
        """Advance the arena simulation one round"""

        self.m_iRound += 1

        # Get all of the units and create a sorted list of their positions
        #  to operate on (reading order)

        lEntityUnit = self.LGoblin() + self.LElf()
        lPos = [x.m_pos for x in lEntityUnit]
        lPos.sort(key=lambda pos: (pos[1], pos[0]))

        # Iterate through positions that need to be updated and run the actions for the unit (if applicable)

        for pos in lPos:
            entity = self.m_mpPosEntity[pos]
            if entity.m_etype not in set(['G', 'E']):
                continue

            entity.Advance()

            if self.m_fEndCombat:
                return

    def SetElfDamage(self, dHp):
        for entity in self.LElf():
            entity.m_dHp = dHp

    def Round(self):
        return self.m_iRound

    def LGoblin(self):
        return [x for x in self.m_mpPosEntity.values() if x.m_etype == 'G']

    def LElf(self):
        return [x for x in self.m_mpPosEntity.values() if x.m_etype == 'E']
        
    def Print(self):
        print "Round", self.m_iRound
        posMax = max(self.m_mpPosEntity.keys())
        for y in range(posMax[1] + 1):
            lHp = []
            for x in range(posMax[0] + 1):
                entity = self.m_mpPosEntity[(x,y)]
                sys.stdout.write(entity.m_etype)
                if entity.m_etype in set(['G', 'E']):
                    lHp.append(entity.m_hp)

            if lHp:
                sys.stdout.write(' {l}'.format(l=str(lHp)))

            sys.stdout.write('\n')

def Day15a():
    """Run a little move/combat simulation and output a code representing information about the outcome"""

    arena = Arena15(ain.s_strIn15)

    #arena.Print()

    while True:
        arena.Advance()

        #arena.Print()

        if arena.m_fEndCombat:
            break

    iRound = arena.Round() - 1  # don't include the round that ended the combat

    winner = 'elf'
    lEntity = arena.LElf()
    if not lEntity:
        winner = 'goblin'
        lEntity = arena.LGoblin()

    hpRemain = sum([e.m_hp for e in lEntity])

    # Hmm. Came up with 225678, but apparently that answer is too high. Not sure what happened, since I actually
    #  calculated something. :/

    # I'm going to try a couple of the other example inputs and see if there's something systematically wrong with my code or my
    #  understanding of the rules.

    # Yep, I get the wrong answer on the first simple one, too, because I'm off by 3hp. Hmm.

    # Likewise, the annotated combat example indicates that I have the movement rules incorrect somehow. Even by round 2, I have a
    #  different configuration of the board than expected.

    # I fixed an error in how I was sorting moves, which corrected a couple examples, but I still had others that were doing the wrong
    #  thing. I figured out then that I had a mistake in the order in which I was going through units (I was rotated 90 degrees from
    #  reading order), and now at least all of the examples I've tried are working.

    # Yes! OK, I have all of the (currently known) bugs worked out. It feels a little slow, but otherwise seems to work OK.

    print "{r} rounds of fighting, with {h} remaining, so {v} wins with a score of {s}".format(r=iRound, h=hpRemain, v=winner, s=iRound * hpRemain)

def Day15b():
    """OK, do the battle, but calculate how much damage the elves need to do to just barely not suffer any losses"""

    arena0 = Arena15(ain.s_strIn15)

    cElf = len(arena0.LElf())

    dHpMax = 100
    dHpMin = 4
    dHp = (dHpMax + dHpMin) / 2

    fFoundMin = False
    while not fFoundMin:
        print "Trying at damage = {d}".format(d=dHp)

        arena1 = Arena15(ain.s_strIn15)
        arena1.SetElfDamage(dHp)

        while True:
            arena1.Advance()

            if cElf != len(arena1.LElf()):
                # lost an elf, so bump their damage up
                dHpMin = dHp + 1

                print "...lost an elf, bumping min up"

                if dHpMin >= dHpMax:
                    assert dHpMin == dHpMax

                break

            if arena1.m_fEndCombat:
                if dHp > dHpMin:
                    # elves won, see if we can reduce their damage
                    print "...elves won, reducing max"
                    dHpMax = dHp
                else:
                    # calculated!
                    fFoundMin = True

                break

        # adjust damage and try again

        dHp = (dHpMax + dHpMin) / 2

    iRound = arena1.Round() - 1  # don't include the round that ended the combat

    winner = 'elf'
    lEntity = arena1.LElf()
    if not lEntity:
        winner = 'goblin'
        lEntity = arena1.LGoblin()

    hpRemain = sum([e.m_hp for e in lEntity])

    print "{r} rounds of fighting, with {h} remaining, so {v} wins with a score of {s}".format(r=iRound, h=hpRemain, v=winner, s=iRound * hpRemain)

class Op16: # tag = op

    OPK_addr = 'addr'
    OPK_addi = 'addi'

    OPK_mulr = 'mulr'
    OPK_muli = 'muli'

    OPK_banr = 'banr'
    OPK_bani = 'bani'

    OPK_borr = 'borr'
    OPK_bori = 'bori'

    OPK_setr = 'setr'
    OPK_seti = 'seti'

    OPK_gtir = 'gtir'
    OPK_gtri = 'gtri'
    OPK_gtrr = 'gtrr'

    OPK_eqir = 'eqir'
    OPK_eqri = 'eqri'
    OPK_eqrr = 'eqrr'

    s_mpOpkFn = {
            OPK_addr : lambda self, a, b: self.GetReg(a) + self.GetReg(b),
            OPK_addi : lambda self, a, b: self.GetReg(a) + b,

            OPK_mulr : lambda self, a, b: self.GetReg(a) * self.GetReg(b),
            OPK_muli : lambda self, a, b: self.GetReg(a) * b,

            OPK_banr : lambda self, a, b: self.GetReg(a) & self.GetReg(b),
            OPK_bani : lambda self, a, b: self.GetReg(a) & b,

            OPK_borr : lambda self, a, b: self.GetReg(a) | self.GetReg(b),
            OPK_bori : lambda self, a, b: self.GetReg(a) | b,

            OPK_setr : lambda self, a, b: self.GetReg(a),
            OPK_seti : lambda self, a, b: a,

            OPK_gtir : lambda self, a, b: 1 if a > self.GetReg(b) else 0,
            OPK_gtri : lambda self, a, b: 1 if self.GetReg(a) > b else 0,
            OPK_gtrr : lambda self, a, b: 1 if self.GetReg(a) > self.GetReg(b) else 0,

            OPK_eqir : lambda self, a, b: 1 if a == self.GetReg(b) else 0,
            OPK_eqri : lambda self, a, b: 1 if self.GetReg(a) == b else 0,
            OPK_eqrr : lambda self, a, b: 1 if self.GetReg(a) == self.GetReg(b) else 0,
        }

    def __init__(self, opk):

        # initialize object; set up fn to match the opk

        self.m_opk = opk
        self.m_fn = Op16.s_mpOpkFn[opk]
        self.m_reg = [0] * 4

    def Apply(self, a, b, c):
        """Apply the op to the given inputs, modifying the internal register to match"""

        res = self.m_fn(self, a, b)
        self.m_reg[c] = res

    def Matches(self, reg0, reg1, a, b, c):
        """returns True if this op produces reg1 from reg0 with the given a, b, c values, and False if not; internal register is modified"""

        self.m_reg = []
        self.m_reg.extend(reg0)
        self.Apply(a, b, c)
        return self.m_reg == reg1

    def GetReg(self, r):
        """Returns the value of the given register"""

        return self.m_reg[r]

    def Evaluate(self, mpOpcodeOp, lOp):
        # register is already set up, so run through ops doing the appropriate apply action

        for op in lOp:
            opk = mpOpcodeOp[op[0]].m_opk
            fn = Op16.s_mpOpkFn[opk]
            self.m_reg[op[3]] = fn(self, op[1], op[2])
            print opk, self.m_reg

def Parse16():
    """Return the list of tests in day 16 input and the list of ops as a tuple of two lists"""

    # extract the before/op/after triples from the input and the ops

    s_reReg = re.compile(r'\S+:\s*\[(\d+),\s*(\d+),\s*(\d+),\s*(\d+)')

    class Test:
        pass

    lTest = []
    lOp = []
    fInTest = False
    for str0 in ain.s_strIn16.strip().split('\n'):
        if str0.strip() == '':
            continue

        if str0.startswith('Before:'):
            fInTest = True
            match = s_reReg.search(str0)
            assert match
            lTest.append(Test())
            lTest[-1].m_reg0 = [int(x) for x in match.groups()]
        elif str0.startswith('After:'):
            fInTest = False
            match = s_reReg.search(str0)
            assert match
            lTest[-1].m_reg1 = [int(x) for x in match.groups()]
        elif fInTest:
            lTest[-1].m_op = [int(x) for x in str0.strip().split()]
        else:
            lOp.append([int(x) for x in str0.strip().split()])

    return (lTest, lOp)

def Day16a():
    """Return the number of samples in the input which behave like three or more opcodes"""

    lTest, lOp = Parse16()

    print "Found {0} tests".format(len(lTest))

    # construct a set of test opcode evaluators

    lOp = [Op16(x) for x in Op16.s_mpOpkFn.keys()]

    # apply the tests and count how many match more than three opcodes

    cMatch = 0
    for test in lTest:
        cCur = 0
        for op in lOp:
            if op.Matches(test.m_reg0, test.m_reg1, test.m_op[1], test.m_op[2], test.m_op[3]):
                cCur += 1
                if cCur > 2:
                    cMatch += 1
                    break

    # Hmm. First answer guess was 656, which was too high, so apparently I have something wrong somewhere. Great.

    # Ah, ha! Forgot the first rule of python, which is that everything is a reference. I was modifying the test input
    #  as things went along because of assigning it to the register for the opcode. Whee!

    print "Found {c} tests that matched 3 or more opcodes".format(c=cMatch)

def Day16b():
    """Using the examples, figure out which opcode number is which opcode, and then run the test code and report the value in register 0 at the end"""

    lTest, lOp = Parse16()

    # Figure out which opcode numbers can be which opcodes

    lOpEval = [Op16(x) for x in Op16.s_mpOpkFn.keys()]

    mpOpcodeSetOp = {}

    for test in lTest:
        setOpCur = set()
        for op in lOpEval:
            if op.Matches(test.m_reg0, test.m_reg1, test.m_op[1], test.m_op[2], test.m_op[3]):
                setOpCur.add(op)

        mpOpcodeSetOp.setdefault(test.m_op[0], set(lOpEval)).intersection_update(setOpCur)

    # Now, start cementing which is which by assigning things that only have one possibility,
    #  removing those from all the rest, and so forth

    mpOpcodeOp = {}
    while len(mpOpcodeSetOp) > 0:
        # find an opcode that only has one possibility in its set
        for opcode, setOp in mpOpcodeSetOp.items():
            if len(setOp) > 1:
                continue

            op = list(setOp)[0]
            mpOpcodeOp[opcode] = op
            del mpOpcodeSetOp[opcode]
            break

        for setOp in mpOpcodeSetOp.values():
            if op in setOp:
                setOp.remove(op)

        print "Assigned opcode {o} to {opk}".format(o=opcode, opk=op.m_opk)

    # Set up a single opcode to do our evaluation

    opEval = Op16(Op16.OPK_addr)    # exact type doesn't matter
    opEval.Evaluate(mpOpcodeOp, lOp)

if __name__ == '__main__':
    Day16a()
    Day16b()
