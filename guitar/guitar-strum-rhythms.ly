% https://lilypond.org/doc/v2.21/Documentation/snippets/rhythms#rhythms-guitar-strum-rhythms

\version "2.22.2" % TODO: can this be defined via common include?

\include "../common.ly"
\include "predefined-guitar-fretboards.ly"

% TODO: pass in chords and rhythm as variables.
% (Using \Chords below throws error: why?)
% Chords = { c1 | g | a:m | f }
Rhythm = { c4 c8 c8 c4 c8 c8 }

<<
  \new ChordNames {
    \chordmode {
      % \Chords % TODO: why does this throw an error? Make it work!
      c1 | g | a:m | f
    }
  }
  \new FretBoards {
    \chordmode {
      % \Chords
      c1 | g | a:m | f
    }
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