#(ly:set-option 'crop #t)

\version "2.22.2"

\header {
    % Remove default LilyPond tagline
    tagline = ##f
}

scale = \relative {
    \key c \major
    \override Fingering.direction = #UP

    c'8-1 d e-3 f-1 g a b-4 c-5
    b-4 a g f-1 e-3 d c4-1
}

\score {
    \new Staff \scale    
    \layout {
        \context {
            \Staff
            \remove "Time_signature_engraver"
            \remove "Bar_engraver"
        }
    }
}
