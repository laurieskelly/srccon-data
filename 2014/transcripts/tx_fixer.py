import os

filenames = [f for f in os.listdir('./raw_originals/') if f.endswith('.md')]

for filename in filenames: 
    out = ''
#    out_of_header = False
    unnamed_speaker_block = False
    with open('./raw_originals/'+filename,'r') as infile:
        for line in infile:
            if line.strip() == '': continue

            line = line.lstrip().replace('\r\n','  \r\n')
            
            # boolean to tell you if the line has a named speaker
            colon_split = line.split(':')
            named_speaker_line = len(colon_split) > 1 and colon_split[0].upper()==colon_split[0]
            if named_speaker_line:
                unnamed_speaker_block = False

            # line could start with one, two, or no '>'s
            gt_marker = None
            for marker in ['>','>>']:
                if line.startswith(marker):
                    gt_marker = marker
                    unnamed_speaker_block = True

            if gt_marker:
                # if not out_of_header: 
                #     out_of_header = True
                if named_speaker_line:
                    # special case for if there is accidentally an 
                    # angle bracket in front of a named speaker
                    line = line[1:].lstrip()
                else:
                    line = '\n>&gt;'+line[len(gt_marker)+1:]+'\n'

            if not gt_marker and not named_speaker_line:
                # paragraph continuation for same speaker should not jump out of block quote
                if unnamed_speaker_block:
                    line = '\n>'+line

                # if line.strip() == '--': 
                #     out_of_header = True

                line = '\n'+line

            #     line = '\n\n'+line[0]+'\\'+line[1:]
            out += line


            

        new_filename = filename.split('.')
        new_filename.insert(1,'_fixed.')
        new_filename = ''.join(new_filename)

        with open(new_filename,'w') as outfile:
            outfile.write(out)
