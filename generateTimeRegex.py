from datetime import date,timedelta


def days_till_end_of_month(y,m,d):
  if d==1:
    return [str(y)+'%02d'%m+'*']

  curr_d = date(y,m,d)
  delta = timedelta(days=1)
  l = []
  while curr_d.month==m:
    l.append(date.strftime(curr_d,"%Y%m%d")+'*')
    curr_d = curr_d + delta
  return l


def days_from_start_of_month(y,m,d):
  end_d = date(y,m,d)
  delta = timedelta(days=1)
  if (end_d+delta).month!=end_d.month:
  	return [str(y)+'%02d'%m+'*']
  l = []
  curr_d = date(y,m,1)
  while curr_d.day<=d:
    l.append(date.strftime(curr_d,"%Y%m%d")+'*')
    curr_d = curr_d + delta
  return l


def months_till_end_of_year(y,m):
  if m==1:
    return str(y)+'*'
  
  l = [str(y)+'%02d'%m+'*']
  while m < 12:
    m += 1
    l.append(str(y)+'%02d'%m+'*')
  return l


def months_from_start_of_year(y,m):
  if m==12:
    return [str(y)+'*']
  
  return [str(y)+'%02d'%mon+'*' for mon in range(1,m+1)]


def generate_date_range(t0,t1):
  
  if int(t0)>=int(t1):
    return []

  y0 = int(t0[:4])
  m0 = int(t0[4:6])
  d0 = int(t0[6:])
  
  y1 = int(t1[:4])
  m1 = int(t1[4:6])
  d1 = int(t1[6:])
  
  l = []
  if y1 > y0:
    l.extend(days_till_end_of_month(y0,m0,d0))
    if m0 < 12:
      l.extend(months_till_end_of_year(y0,m0+1))
    curr_y = y0 + 1
    while curr_y < y1:
      l.append(str(curr_y)+'*')
      curr_y = curr_y + 1
    if m1==1:
      l.extend(days_from_start_of_month(y1,m1,d1))
    else:
      l.extend(months_from_start_of_year(y1,m1-1))
      l.extend(days_from_start_of_month(y1,m1,d1))
  elif m1==m0:
    delta = timedelta(days=1)
    curr_d = date(y0,m0,d0)
    while curr_d.day<=d1:
      l.append(date.strftime(curr_d,"%Y%m%d")+'*')
      curr_d = curr_d + delta
  else:
      l.extend(days_till_end_of_month(y0,m0,d0))
      curr_m = m0 + 1
      while curr_m < m1:
        l.append(str(y1)+'%02d'%curr_m+'*')
        curr_m = curr_m + 1
      l.extend(days_from_start_of_month(y1,m1,d1))
  
  return l
