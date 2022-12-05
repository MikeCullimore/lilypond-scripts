% https://lilypond.org/doc/v2.21/Documentation/snippets/rhythms#rhythms-guitar-strum-rhythms

\version "2.22.2" % TODO: can this be defined via common include?

\include "../common.ly"
\include "guitar-strum-rhythms-inputs.ly"
\include "predefined-guitar-fretboards.ly"

<<
  \new ChordNames {
    \Chords
  }
  \new FretBoards {
    \Chords
  }
  \new Voice \with {
    \consists "Pitch_squash_engraver"
  } {
    {
      \improvisationOn
      \Rhythm
      \Rhythm
      \Rhythm
      \Rhythm
    }
  }
>>