import React from 'react';
import { Grid, Box, Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useHistory, Link } from 'react-router-dom';

const useStyles = makeStyles(() => ({
  box: {
    overflowX: 'hidden',
    overflowY: 'hidden',
  },
  logo: {
    fontSize: '36px',
    fontWeight: 'bolder',
    color: '#C4C5D1',
  },
  listItemPrimary: {
    display: 'grid',
    placeItems: 'center',
    height: '150px',
  },
  listItem: {
    display: 'grid',
    placeItems: 'center',
    height: '150px',
    fontFamily: 'Lato',
    '&:hover': {
      backgroundColor: '#F0F0F3',
      cursor: 'pointer',
    },
  },
  logoIcons: {
    height: '70px',
    width: '70px',
    backgroundImage:
      'linear-gradient(224.38deg, #E9E9E9 5.75%, #E9E9E9 93.61%)',
    borderRadius: '20px',
    textAlign: 'center',
    display: 'grid',
    placeItems: 'center',
  },
  listText: {
    fontSize: '17px',
    color: '#ffffff',
    '&:hover': {
      color: '#00293B',
    },
  },
  listItemActive: {
    display: 'grid',
    placeItems: 'center',
    height: '150px',
    backgroundColor: '#F0F0F3',
    fontFamily: 'Lato',
    '&:hover': {
      cursor: 'pointer',
    },
  },
  logoIconsActive: {
    height: '70px',
    width: '70px',
    backgroundImage:
      'linear-gradient(224.38deg, #E9E9E9 5.75%, #E9E9E9 93.61%)',
    borderRadius: '20px',
    textAlign: 'center',
    display: 'grid',
    placeItems: 'center',
    boxShadow:
      '10px 10px 30px rgba(174, 174, 192, 0.4), -10px -10px 30px #FFFFFF',
  },
  listTextActive: {
    fontSize: '17px',
    color: '#00293B',
  },
}));

const Sidebar = () => {
  const classes = useStyles();
  const history = useHistory();
  const path = history.location.pathname;
  const pathHead = history.location.pathname.split('/')[1];
  return (
    <>
      {console.log(pathHead)}
      <Box className={classes.box}>
        <Grid container spacing={2}>
          <Grid item xs={12} className={classes.listItemPrimary}>
            <h1 className={classes.logo}>Vexio</h1>
          </Grid>
          <Grid
            item
            xs={12}
            className={
              path === '/dashboard/home'
                ? classes.listItemActive
                : classes.listItem
            }
            onClick={() => {
              history.push('/dashboard/home');
            }}
          >
            <Paper
              elevation={0}
              className={
                path === '/dashboard/home'
                  ? classes.logoIconsActive
                  : classes.logoIcons
              }
            >
              <i className="fas fa-book fa-2x" style={{ color: '#00293B' }} />
            </Paper>
            <h2
              className={
                path === '/dashboard/home'
                  ? classes.listTextActive
                  : classes.listText
              }
            >
              Home
            </h2>
          </Grid>
          <Grid item xs={12} className={classes.listItem}>
            <Paper elevation={0} className={classes.logoIcons}>
              <i className="fas fa-book fa-2x" style={{ color: '#00293B' }} />
            </Paper>
            <h2 className={classes.listText}>Courses</h2>
          </Grid>
          <Grid
            item
            xs={12}
            className={
              path === '/dashboard/timetable'
                ? classes.listItemActive
                : classes.listItem
            }
            onClick={() => {
              history.push('/dashboard/timetable');
            }}
          >
            <Paper
              elevation={0}
              className={
                path === '/dashboard/timetable'
                  ? classes.logoIconsActive
                  : classes.logoIcons
              }
            >
              <i className="fas fa-book fa-2x" style={{ color: '#00293B' }} />
            </Paper>

            <h2
              className={
                path === '/dashboard/timetable'
                  ? classes.listTextActive
                  : classes.listText
              }
            >
              TimeTable
            </h2>
          </Grid>
          <Grid
            item
            xs={12}
            className={
              pathHead === 'forum' ? classes.listItemActive : classes.listItem
            }
            onClick={() => {
              history.push('/forum/forum-details');
            }}
          >
            <Paper
              elevation={0}
              className={
                pathHead === 'forum'
                  ? classes.logoIconsActive
                  : classes.logoIcons
              }
            >
              <i className="fas fa-book fa-2x" style={{ color: '#00293B' }} />
            </Paper>
            <h2
              className={
                pathHead === 'forum' ? classes.listTextActive : classes.listText
              }
            >
              Forums
            </h2>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};

export default Sidebar;
