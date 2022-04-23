from driver import *
import time

if __name__ == '__main__':
    time_start = time.time_ns()
    f_in = 'wp.txt'
    f_encoded = 'wp_e.txt'
    f_decoded = 'wp_e_d.txt'
    sys.argv.append('-e')
    sys.argv.append(f_in)
    main()
    print(f'Encoding time:{(time.time_ns() - time_start)/10**9} sec.')
    time_start = time.time_ns()
    sys.argv[1] = '-d'
    sys.argv[2] = f_encoded
    main()
    print(f'Decoding time:{(time.time_ns() - time_start)/10**9} sec.')
    time_start = time.time_ns()

    with open(f_in, 'r', encoding='utf-8') as f1:
        with open(f_decoded, 'r', encoding='utf-8') as f2:
            src = f1.read()
            decoded = f2.read()
            if src != decoded:
                print('ERROR: the source and decoded result are not identical!')
            else:
                print('OKAY!')
    print(f'File comparing time:{(time.time_ns() - time_start)/10**9} sec.')