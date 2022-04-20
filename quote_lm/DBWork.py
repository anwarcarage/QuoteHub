import sqlite3
from .models import QuoteLm


def hours_calculate(track_id):
    # connect to database
    conn = sqlite3.connect(database='db.sqlite3')
    # create cursor object
    cursor = conn.cursor()
    # grab row that matches quote_id with track_id
    output = QuoteLm.objects.get(id=track_id)

    # assigning database data to variables
    drill_bar_num = output.drill_bar_num
    h_headers = output.h_headers
    height = output.height
    length = output.length
    material = output.material
    surface_finish = output.surface_finish
    v_headers = output.v_headers
    width = output.width

    # math out hours using user input values
    quote_id_id = track_id
    weld_hours = calc_weld(material, length, width, height, h_headers, v_headers)
    fit_hours = weld_hours // 2
    machine_hours = calc_nc(material, length, width, drill_bar_num)
    program_hours = machine_hours // 4
    bench_hours = calc_bench(material, length, width, surface_finish)
    assembly_hours = calc_assembly(length, width, material, drill_bar_num)
    shipping_hours = calc_shipping(length, width, height)
    laser_hours = calc_laser(length, width)
    inspect_hours = calc_qa(length, width)
    total_hours = (weld_hours + fit_hours + machine_hours + program_hours + bench_hours + assembly_hours +
                   shipping_hours + laser_hours + inspect_hours)

    price = calc_price(weld_hours, fit_hours, machine_hours, program_hours, bench_hours, assembly_hours, shipping_hours,
                       laser_hours, inspect_hours, track_id)

    # populate calchour table
    cursor.execute('INSERT INTO quote_lm_calchour(weld_hours, fit_hours, program_hours, machine_hours, '
                   'bench_hours, assembly_hours, shipping_hours, laser_hours, inspect_hours, total_hours, quote_id_id) '
                   'VALUES(?,?,?,?,?,?,?,?,?,?,?)', (weld_hours, fit_hours, program_hours, machine_hours, bench_hours,
                                                     assembly_hours, shipping_hours, laser_hours, inspect_hours,
                                                     total_hours, quote_id_id))
    # populate calcprice table
    cursor.execute('INSERT INTO quote_lm_calcprice(weld_price, fit_price, program_price, machine_price, '
                   'bench_price, assembly_price, shipping_price, laser_price, inspect_price, total_price, quote_id_id)'
                   'VALUES(?,?,?,?,?,?,?,?,?,?,?)', price)

    # commit changes
    conn.commit()
    # close database connection
    conn.close()


def update_calculate(track_id):
    # connect to database
    conn = sqlite3.connect(database='db.sqlite3')
    # create cursor object
    cursor = conn.cursor()
    # grab row that matches quote_id with track_id
    output = QuoteLm.objects.get(id=track_id)

    # assigning database data to variables
    drill_bar_num = output.drill_bar_num
    h_headers = output.h_headers
    height = output.height
    length = output.length
    material = output.material
    surface_finish = output.surface_finish
    v_headers = output.v_headers
    width = output.width

    # math out hours using user input values
    quote_id_id = track_id
    weld_hours = calc_weld(material, length, width, height, h_headers, v_headers)
    fit_hours = weld_hours // 2
    machine_hours = calc_nc(material, length, width, drill_bar_num)
    program_hours = machine_hours // 4
    bench_hours = calc_bench(material, length, width, surface_finish)
    assembly_hours = calc_assembly(length, width, material, drill_bar_num)
    shipping_hours = calc_shipping(length, width, height)
    laser_hours = calc_laser(length, width)
    inspect_hours = calc_qa(length, width)
    total_hours = (weld_hours + fit_hours + machine_hours + program_hours + bench_hours + assembly_hours +
                   shipping_hours + laser_hours + inspect_hours)

    price = calc_price(weld_hours, fit_hours, machine_hours, program_hours, bench_hours, assembly_hours, shipping_hours,
                       laser_hours, inspect_hours, track_id)

    # update calchour table
    cursor.execute('UPDATE quote_lm_calchour SET weld_hours=?, fit_hours=?, program_hours=?, machine_hours=?, '
                   'bench_hours=?, assembly_hours=?, shipping_hours=?, laser_hours=?, inspect_hours=?, total_hours=? '
                   ' WHERE quote_id_id=?', (weld_hours, fit_hours, program_hours, machine_hours, bench_hours,
                                             assembly_hours, shipping_hours, laser_hours, inspect_hours,
                                             total_hours, quote_id_id))
    # update calcprice table
    cursor.execute('UPDATE quote_lm_calcprice SET weld_price=?, fit_price=?, program_price=?, machine_price=?, '
                   'bench_price=?, assembly_price=?, shipping_price=?, laser_price=?, inspect_price=?, total_price=? '
                   'WHERE quote_id_id=?', price)

    # commit changes
    conn.commit()
    # close database connection
    conn.close()


# calculates weld hours
def calc_weld(material, length, width, height, h_headers, v_headers):
    if material == 'AL':
        weld_x = (length * h_headers * 3) // 24
        weld_y = (width * v_headers * 3) // 24
        weld_z = (h_headers * v_headers * 2 * height) // 24
        weld_fs = (length // 60) * ((width // 12) * 4)
        weld_hours = weld_x + weld_y + weld_z + weld_fs
        return weld_hours
    elif material == 'STL' or 'INV':
        weld_x = (length * h_headers * 3) // 32
        weld_y = (width * v_headers * 3) // 32
        weld_z = (h_headers * v_headers * 2 * height) // 32
        weld_fs = (length // 60) * ((width // 12) * 4)
        weld_hours = weld_x + weld_y + weld_z + weld_fs
        return weld_hours


# calculates machining hours
def calc_nc(material, length, width, drill_bar_num):
    if material == 'AL':
        nc = (((length * width) // 144) * 1.7) // 1
        sm_nc = drill_bar_num * 4
        machine_hours = nc + sm_nc
        return machine_hours
    elif material == 'STL' or 'INV':
        nc = ((length * width) // 144) * 2
        sm_nc = drill_bar_num * 4
        machine_hours = nc + sm_nc
        return machine_hours


# caculates bench hours
def calc_bench(material, length, width, surface_finish):
    if material == 'AL':
        bench_hours = ((length * width) // 1296) * 8
        if surface_finish == '32RA':
            bench_hours = bench_hours * 2
            return bench_hours
        elif surface_finish == '125RA':
            bench_hours = bench_hours // 2
            return bench_hours
        elif surface_finish == '64RA':
            return bench_hours
    elif material == 'STL':
        bench_hours = ((length * width) // 1296) * 15
        if surface_finish == '32RA':
            bench_hours = bench_hours * 2
            return bench_hours
        elif surface_finish == '125RA':
            bench_hours = bench_hours // 2
            return bench_hours
        elif surface_finish == '64RA':
            return bench_hours
    elif material == 'INV':
        bench_hours = ((length * width) // 1296) * 24
        if surface_finish == '32RA':
            bench_hours = bench_hours * 2
            return bench_hours
        elif surface_finish == '125RA':
            bench_hours = bench_hours // 2
            return bench_hours
        elif surface_finish == '64RA':
            return bench_hours


# calculates assembly and paint hours
def calc_assembly(length, width, material, drill_bar_num):
    if material == 'AL':
        assembly_hours = 20 + ((length * width) // 144) + (drill_bar_num * 4)
        return assembly_hours
    if material == 'STL' or 'INV':
        assembly_hours = 40 + ((length * width) // 144) + (drill_bar_num * 4)
        return assembly_hours


# calculates shipping/crating hours
def calc_shipping(length, width, height):
    cubic_volume = (length * width * height) // 1728
    if cubic_volume <= 64:
        shipping_hours = 12
        return shipping_hours
    elif 64 < cubic_volume <= 200:
        shipping_hours = 24
        return shipping_hours
    elif 200 < cubic_volume <= 300:
        shipping_hours = 32
        return shipping_hours
    elif 300 < cubic_volume < 400:
        shipping_hours = 48
        return shipping_hours
    else:
        shipping_hours = 60
        return shipping_hours


# calculates laser check hours
def calc_laser(length, width):
    laser_hours = 16 + (((length * width) // 144) * .667) // 1
    return laser_hours


# calculates QA inspection hours
def calc_qa(length, width):
    surface_area = length * width
    if surface_area <= 32:
        inspect_hours = 24
        return inspect_hours
    elif 32 < surface_area <= 64:
        inspect_hours = 32
        return inspect_hours
    elif 64 < surface_area <= 128:
        inspect_hours = 48
        return inspect_hours
    else:
        inspect_hours = 60
        return inspect_hours


def calc_price(weld_hours, fit_hours, machine_hours, program_hours, bench_hours, assembly_hours, shipping_hours,
               laser_hours, inspect_hours, track_id):
    weld_price = weld_hours * 70
    fit_price = fit_hours * 70
    program_price = program_hours * 120
    machine_price = machine_hours * 120
    bench_price = bench_hours * 70
    assembly_price = assembly_hours * 70
    shipping_price = shipping_hours * 70
    laser_price = laser_hours * 90
    inspect_price = inspect_hours * 90
    total_hours = weld_price + fit_price + program_price + machine_price + bench_price + assembly_price + \
                  shipping_price + laser_price + inspect_price
    quote_id_id = track_id

    price_output = [weld_price, fit_price, program_price, machine_price, bench_price, assembly_price, shipping_price,
                    laser_price, inspect_price, total_hours, quote_id_id]

    return price_output
