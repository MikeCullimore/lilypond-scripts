\include "template-inputs-test.ly"

% Crop SVG to content.
#(ly:set-option 'crop #t)

\version "2.22.2"

\header {
    % Remove default LilyPond tagline
    tagline = ##f
}

scale = \relative {
    \Key
    \Clef
    \override Fingering.direction = #DOWN
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
