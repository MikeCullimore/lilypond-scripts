% ABRSM scales and arpeggios
% Grade 2
% G major, two octaves, hands together.

% todo
% Port to TypeScript?! Simpler to integrate with React UI, better tools for SVG.
% Lift common config for scale out into common-scales.ly.
% Fingering (how to automate?).
% Import common by absolute path or inject directly?
% White background (edit SVG directly as part of post-processing?)
% Try VS Code minify SVG option.

\version "2.22.2"

\include "../../../common.ly"

common = {
    \key g \major
    \omit Staff.TimeSignature
    % \omit Staff.BarLine % Leaves bar lines between staffs.
    \override Staff.BarLine.break-visibility = ##(#f #f #f)
}

right = \relative {
    \common
    \clef treble
    g8-1 a b c-1 d e fis
    g-1 a b-3 c-1 d e fis
    g-5 fis e d c-1 b-3 a
    g-1 fis-4 e d c-1 b-3 a
    g4
}

left = \relative {
    \common
    \clef bass
    g,8 a b c d e fis
    g a b c d e fis
    g fis e d c b a
    g fis e d c b a
    g4
}

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
