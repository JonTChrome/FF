from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Float
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    home = Column(String(25))
    name = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    
class Player(Base):
    __tablename__ = 'players'
    __table_args__ = {'extend_existing': True} 
    
    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    
    ##Name
    search_full_name = Column(String(255))
    last_name = Column(String(255))
    first_name = Column(String(255))
    search_first_name = Column(String(255))
    search_last_name = Column(String(255))

    ##Ids
    espn_id = Column(String(255))
    gsis_id = Column(String(255))
    yahoo_id = Column(String(255))
    rotoworld_id = Column(String(255))
    fantasy_data_id = Column(String(255))
    rotowire_id = Column(String(255))
    sportradar_id = Column(String(255))
    stats_id = Column(String(255))

    ##body
    height = Column(String(255))
    weight = Column(String(255))
    age = Column(String(255))
    
    ##Origin
    birth_date = Column(String(255))
    birth_country = Column(String(255))
    birth_state = Column(String(255))
    birth_city = Column(String(255))
    high_school = Column(String(255))
    college = Column(String(255))
    years_exp = Column(String(255))
    
    ##Injury
    injury_body_part = Column(String(255))
    injury_start_date = Column(String(255))
    injury_status = Column(String(255))
    injury_notes = Column(String(1000))
    practice_participation = Column(String(255))

    ##Team Status
    team_id = Column(Integer, ForeignKey('teams.id'))
    sport = Column(String(255))
    depth_chart_order = Column(String(255))
    position = Column(String(255))
    depth_chart_position = Column(String(100))
    status = Column(String(100))
    number = Column(String(100))
    practice_description = Column(String(255))

    ##MISC
    active = Column(String(255))
    news_updated = Column(String(255))
    hashtag = Column(String(255))
    search_rank = Column(String(255))
    
    #'fantasy_positions': ['LB'],

    ## injury will link to player and will include an import from player call based on a status change
    ## injury will then populate start date of new and end date of old injury
class Injury(Base):
    __tablename__ = 'injury'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    injury_body_part = Column(String(255))
    injury_notes = Column(String(1000))
    practice_participation = Column(String(255))
    
class Quarterback(Base):
    __tablename__ = "quarterback"
    __table_args__ = {'extend_existing': True} 
    
    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    player_id_local = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    pts_ppr = Column(Float)
    pts_std = Column(Float)
    
    pass_lng = Column(Float)
    off_snp = Column(Float)
    gs = Column(Float)
    cmp_pct = Column(Float)
    pass_fd = Column(Float)
    pass_sack = Column(Float)
    tm_off_snp = Column(Float)
    wind_speed = Column(Float)
    gms_active = Column(Float)
    pass_cmp = Column(Float)
    pts_half_ppr = Column(Float)
    pass_rtg = Column(Float)
    pass_sack_yds = Column(Float)
    tm_def_snp = Column(Float)
    rush_ypa = Column(Float)
    temperature = Column(Float)
    pass_att = Column(Float)
    pass_inc = Column(Float)
    pass_ypa = Column(Float)
    rush_att = Column(Float)
    pass_td = Column(Float)
    rush_lng = Column(Float)
    tm_st_snp = Column(Float)
    rush_yd = Column(Float)
    pass_yd = Column(Float)
    rush_td = Column(Float)
    fum_lost = Column(Float)
    humidity = Column(Float)
    fum = Column(Float)
    pass_ypc = Column(Float)
    
class WideReceiver(Base):
    __tablename__ = "widereceiver"
    __table_args__ = {'extend_existing': True} 

    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    pts_std = Column(Float)
    pts_ppr = Column(Float)
    pts_half_ppr = Column(Float)
    
    wind_speed = Column(Float)
    tm_st_snp = Column(Float)
    tm_off_snp = Column(Float)
    tm_def_snp = Column(Float)
    temperature = Column(Float)
    st_snp = Column(Float)
    rec_ypt = Column(Float)
    rec_ypr = Column(Float)
    rec_yd = Column(Float)
    rec_tgt = Column(Float)
    rec_pct = Column(Float)
    rec_lng = Column(Float)
    rec = Column(Float)
    pr_ypa = Column(Float)
    pr_yd = Column(Float)
    pr_lng = Column(Float)
    pr = Column(Float)
    off_snp = Column(Float)
    humididty = Column(Float)
    gp = Column(Float)
    gs = Column(Float)
    gms_active = Column(Float)
    bonus_rec_yd = Column(Float)
    bonus_rec_wr = Column(Float)
    bonus_rc_yd_100 = Column(Float)
    bonus_rush_rec_yd_100 = Column(Float)
    off_snp = Column(Float)
    idp_tkl_solo = Column(Float)
    idp_tkl = Column(Float)
    td = Column(Float)

class RunningBack(Base):
    __tablename__ = "runningback"
    __table_args__ = {'extend_existing': True} 

    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
            
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    pts_std = Column(Float)
    pts_ppr = Column(Float)
    pts_half_ppr = Column(Float)
    
    wind_speed = Column(Float)
    tm_st_snp = Column(Float)
    tm_off_snp = Column(Float)
    tm_def_snp = Column(Float)
    temperature = Column(Float)
    td = Column(Float)
    rush_ypa = Column(Float)
    rush_yd = Column(Float)
    rush_td = Column(Float)
    rush_lng = Column(Float)
    rush_fd = Column(Float)
    rush_att = Column(Float)
    rush_2pt = Column(Float)
    rec_ypt = Column(Float)
    rec_ypr = Column(Float)
    rec_yd = Column(Float)
    rec_tgt = Column(Float)
    rec_pct = Column(Float)
    rec_lng = Column(Float)
    rec_fd = Column(Float)
    rec = Column(Float)
    off_snp = Column(Float)
    humidity = Column(Float)
    gs = Column(Float)
    gp = Column(Float)
    gms_active = Column(Float)
    bonus_rec_rb = Column(Float)
    
class TightEnd(Base):
    __tablename__ = "tightend"
    __table_args__ = {'extend_existing': True} 

    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
            
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    pts_std = Column(Float)
    pts_ppr = Column(Float)
    pts_half_ppr = Column(Float)
    
    wind_speed = Column(Float)
    tm_st_snp = Column(Float)
    tm_off_snp = Column(Float)
    tm_def_snp = Column(Float)
    temperature = Column(Float)
    td = Column(Float)
    rec_ypt = Column(Float)
    rec_ypr = Column(Float)
    rec_tgt = Column(Float)
    rec_td = Column(Float)
    rec_pct = Column(Float)
    rec_lng = Column(Float)
    rec_fd = Column(Float)
    rec = Column(Float)
    off_snp = Column(Float)
    humidity = Column(Float)
    gs = Column(Float)
    gp = Column(Float)
    gms_active = Column(Float)
    bonus_rec_te = Column(Float)

class Kicker(Base):
    __tablename__ = "kicker"
    __table_args__ = {'extend_existing': True} 

    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
            
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    pts_std = Column(Float)
    pts_ppr = Column(Float)
    pts_half_ppr = Column(Float)
    
    xpm = Column(Float)
    xpa = Column(Float)
    wind_speed =Column(Float)
    tm_st_snp = Column(Float)
    tm_off_snp = Column(Float)
    tm_def_snp = Column(Float)
    temperature = Column(Float)
    st_snp = Column(Float)
    humidity = Column(Float)
    gp = Column(Float)
    gms_active = Column(Float)
    fgm_yds_over_30 = Column(Float)
    fgm_yds = Column(Float)
    fgm_pct = Column(Float)
    fgm_lng = Column(Float)
    fgm_40_49 = Column(Float)
    fgm = Column(Float)
    fga = Column(Float)

class Defense(Base):
    __tablename__ = "defense"
    __table_args__ = {'extend_existing': True} 

    def __init__(self):
        return
    
    def __init__(self, playerDict):
        for column in playerDict:
            setattr(self, column, playerDict[column])
            
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(Integer)
    week = Column(Integer)
    against = Column(String(10))
    
    def_pr_yd = Column(Float)
    def_kr_lng = Column(Float)
    tkl_loss = Column(Float)
    fan_pts_allow_rb = Column(Float)
    down_3_att = Column(Float)
    pts_allow = Column(Float)
    sack_yd = Column(Float)
    ff = Column(Float)
    def_kr_yd = Column(Float)
    fan_pts_allow_k = Column(Float)
    int_ret_yd = Column(Float)
    fan_pts_allow_qb = Column(Float)
    fan_pts_allow = Column(Float)
    def_pass_def = Column(Float)
    down_4_conv = Column(Float)
    down_4_att = Column(Float)
    wind_speed = Column(Float)
    pts_half_ppr = Column(Float)
    fum_rec = Column(Float)
    qb_hit = Column(Float)
    temperature = Column(Float)
    def_pr = Column(Float)
    tkl_solo = Column(Float)
    int = Column(Float)
    def_pr_lng = Column(Float)
    tkl_ast = Column(Float)
    def_kr = Column(Float)
    sack = Column(Float)
    fan_pts_allow_wr = Column(Float)
    pts_allow_14_20 = Column(Float)
    fan_pts_allow_te = Column(Float)
    yds_allow = Column(Float)
    yds_allow_200_299 = Column(Float)
    humidity = Column(Float)
    pts_std = Column(Float)
    down_3_conv = Column(Float)
    

def getBase():
    return Base