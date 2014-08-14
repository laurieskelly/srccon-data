import os

filenames = [f for f in os.listdir('.') if f.endswith('.md') and not f.endswith('fixed.md')]

for filename in filenames: 
    out = ''
    with open(filename,'r') as infile:


        for line in infile:
            if line.startswith('['): 
                line = line.replace(']',']  ')
            line.replace('\r\n','  \r\n')

            if line.startswith('>>'):
                line = '\n'+line[0]+'\\'+line[1:]


            out += line


        new_filename = filename.split('.')
        new_filename.insert(1,'_fixed.')
        new_filename = ''.join(new_filename)

        with open(new_filename,'w') as outfile:
            outfile.write(out)
