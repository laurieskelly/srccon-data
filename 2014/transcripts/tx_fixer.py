import os

filenames = [f for f in os.listdir('./raw_originals/') if f.endswith('.md')]

for filename in filenames: 
    out = ''
    with open('./raw_originals/'+filename,'r') as infile:

        for line in infile:
            line = line.lstrip().replace('\r\n','\r\n\n')
            
            for gt_marker in ['>','>>']:
                if line.startswith(gt_marker):
                    line = '\n>&gt;'+line[len(gt_marker)+1:]+'\n'

            #     line = '\n\n'+line[0]+'\\'+line[1:]
            out += line

            


        new_filename = filename.split('.')
        new_filename.insert(1,'_fixed.')
        new_filename = ''.join(new_filename)

        with open(new_filename,'w') as outfile:
            outfile.write(out)
