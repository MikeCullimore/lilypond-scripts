% Sight reading exercise
% Trinity grade two book
% Exercise 45

\version "2.22.2"

\include "../../common.ly"

common = {
    \key f \major
    \time 4/4
    \numericTimeSignature
}

right = \relative {
    \common
    \clef treble
    r1\p
    f'4-3\<(e f4. g8
    a4\mf\!) f(e8\> f g a
    f2) f\p\!
}

left = \relative {
    \common
    \clef bass
    f4-3(e f4. g8
    a2 f ~
    f4) a(g e
    f a f2)
}

\markup "Moderato espressivo"
\score {
    \new PianoStaff
    <<
        \new Staff \right
        \new Staff \left
    >>
    \layout {
        \context {
            \Staff
        }
    }
    \midi {}
}
