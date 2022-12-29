# TODO: copy each file (except template) to tmp.ly
# Run Lilypond on template
# Delete tmp.ly
tmp_filename='template-inputs.ly'
for input_file in *.ly; do
    # TODO: skip template itself.
    cp $input_file $tmp_filename
    output_file=$(basename "$input_file" .ly)
    # echo $output_file
    # TODO: pass output filename (replace input extension with *.svg)
    lilypond --svg --output=$output_file $tmp_filename
done
# rm $tmp_filename