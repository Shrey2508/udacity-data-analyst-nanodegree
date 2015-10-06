import csv

def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.

    For example, if file_1 has:
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w') as master_file:
        writer_out = csv.writer(master_file, delimiter=',')
        writer_out.writerow(['C/A', 'UNIT', 'SCP', 'DATEn', 'TIMEn', 'DESCn', 'ENTRIESn', 'EXITSn'])

        for filename in filenames:
            f_in = open(filename, 'r')
            reader_in = csv.reader(f_in, delimiter=',')
            for line in reader_in:
                writer_out.writerow(line)

if __name__ == '__main__':
