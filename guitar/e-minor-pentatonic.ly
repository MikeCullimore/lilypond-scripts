\version "2.22.2"

\include "../common.ly"

staffMusic = \relative {
  e g-2 a b-1 d
  e-1 g a-1 b d-2
  e g-2
}

tabMusic = \relative {
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