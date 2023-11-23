\version "2.22.2"

\include "../common.ly"

staffMusic = \relative {
  \key e \minor
  e8 g-2 a b-1 d
  e-1 g a-1 b d-2
  e g-2
}

% TAB is deliberately shown an octave above to reduce ledger lines.
tabMusic = \relative {
  \key e \minor
  e, g a b d
  e g a b d
  e g
}

\new StaffGroup \with {
  \omit Staff.BarLine
  \omit StaffGroup.SpanBar
  \override TimeSignature.stencil = ##f
}
<<
  \new Staff {
    \staffMusic
  }
  \new TabStaff {
    \tabMusic
  }
>>