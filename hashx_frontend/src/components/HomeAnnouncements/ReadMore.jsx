import React from 'react';
import { Grid, Divider, Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import { motion } from 'framer-motion';

const useStyles = makeStyles(() => ({
  btn: {
    borderRadius: '25px',
    height: '25px',
    width: '100%',
    background: '#FFFFFF',
    // boxShadow: '-6px -6px 16px #fff, 6px 6px 16px #d1cdc7',
  },
  btnText: {
    fontSize: '14px',
    fontWeight: 'bold',
  },
  btnContainer: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-around',
    padding: '2px 10px',
  },
  motionContainer: {
    cursor: 'pointer',
  },
}));

const CoursesCard = (props) => {
  const classes = useStyles();
  return (
    <motion.div
      className={classes.motionContainer}
      whileTap={{ scale: 0.8 }}
      whileHover={{ rotate: 360 }}
    >
      <Grid container className={classes.btn}>
        <Grid item xs={12} className={classes.btnContainer}>
          <div className={classes.btnText}>Explore&nbsp;</div>
          <div className={classes.arrowContainer}>
            <ArrowForwardIcon fontSize="inherit" className={classes.arrow} />
          </div>
        </Grid>
      </Grid>
    </motion.div>
  );
};

export default CoursesCard;
