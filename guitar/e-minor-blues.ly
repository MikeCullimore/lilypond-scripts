\version "2.22.2"

\include "../common.ly"

% Choose English for more familiar note names.
\language "english"

staffMusic = \relative {
  \key e \minor
  e8 g-2 a bf-1 b-2 d
  e-2 g a-1 bf-2 b d-2
  e g-2
}

% TAB is deliberately shown an octave above to reduce ledger lines.
tabMusic = \relative {
  \key e \minor
  e, g a bf b d
  e g a bf b d
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