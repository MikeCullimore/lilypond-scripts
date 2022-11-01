#(ly:set-option 'crop #t)

\version "2.22.2"

\header {
    % Remove default LilyPond tagline
    tagline = ##f
}

scale = \relative {
    \key c \major
    \clef bass
    \override Fingering.direction = #DOWN

    c8-5 d e f g-1 a-3 b c-1
    b a-3 g-1 f e d c4-5
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
