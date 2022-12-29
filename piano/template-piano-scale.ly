\version "2.22.2"

\include "../common.ly"
\include "template-inputs.ly"

scale = \relative {
    \Key
    \Clef
    \Scale
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
    \midi {}
}
