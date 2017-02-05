import numpy as np

def extract_time_info(row):
    
    # date and time info
    if row.createdAt is np.nan:
        row["year"] = np.nan
        row["month"] = np.nan
        row["day"] = np.nan
        row["week_number"] = np.nan
        row["hour"] = np.nan
    else:
        date_time = row.createdAt.split(" ")
        date = date_time[0].split("-")
        if len(date)!=3:  # bad values
            row["year"] = np.nan
            row["month"] = np.nan
            row["day"] = np.nan
            row["week_number"] = np.nan
            row["hour"] = np.nan
        else:
            try:
                year = int(date[0])
            except:
                year = np.nan
            try:
                month = int(date[1])
            except:
                month = np.nan
            try:
                day = int(date[2])
            except:
                day = np.nan
            if year > 2000 and year < 2017:
                row["year"] = year
            else:
                row["year"] = np.nan
            if month > 0 and month < 13:
                row["month"] = month
            else:
                row["month"] = np.nan
            if day > 0 and day < 32:
                row["day"] = day
            else:
                row["day"] = np.nan
            if pd.notnull(row["year"]) and pd.notnull(row["month"]) and pd.notnull(row["day"]):
                row["week_number"] = datetime.date(year, month, day).isocalendar()[1]
            else:
                row["week_number"] = np.nan
            # extract time
            if len(date_time) > 1:
                hour = int(date_time[1].split(":")[0])
                if hour >= 0 and hour < 25:
                    row["hour"] = hour
                else:
                    row["hour"] = np.nan
            else:
                row["hour"] = np.nan
    
    return row


def extract_location(row):
    
    global num_processed
    num_processed += 1
    if num_processed % 1000 == 0:
        print("Number of rows processed: %d/%d" % (num_processed,num_entries))
    
    lat = float("%.2f" % float(row.placeLatitude))
    long = float("%.2f" % float(row.placeLongitude))
    lat_long = str(lat)+"_"+str(long)
    if lat_long in df_cities.index:
        row["city"] = df_cities.loc[lat_long].city
        row["state"] = df_cities.loc[lat_long].state
        row["country"] = df_cities.loc[lat_long].country
        return row
    
    
    # IF NEW PAIR OF COORDINATES        
    location = geolocator.reverse((lat,long), timeout=60)
            
    # city / town / village
    vals = ["city", "town", "village"]
    for city in vals:
        try:
            row["city"] = location.raw['address'][city]
            break
        except:
            row["city"] = np.nan
            continue
            
    # country
    try:
        row["country"] = location.raw['address']["country_code"]
    except:
        row["country"] = np.nan
    
    # state / county
    vals = ["state", "county"]
    for state in vals:
        try:
            row["state"] = location.raw['address'][state]
            break
        except:
            row["state"] = np.nan
            continue
            
    time.sleep(1)
    
    df_cities.loc[lat_long] = [row["city"], row["state"], row["country"]]
    
    return row