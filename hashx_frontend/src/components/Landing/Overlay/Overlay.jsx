import React, { useRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { useSpring, useTrail, config, animated, useChain } from 'react-spring';
import background from '../../../assets/Overlay-menu/Sun-Tornado.svg';

const useStyles = makeStyles((theme) => ({
  root: {
    zIndex: 99,
    position: 'absolute',
    right: '0%',
    top: '0%',
    backgroundColor: 'black',
    backgroundAttachment: 'fixed',
    backgroundSize: 'cover',
  },
  items: {
    display: 'flex',
    flexDirection: 'column',
    height: '100%',
    width: '100%',

    [theme.breakpoints.down('sm')]: {
      fontSize: '52px',

      overflow: 'hidden',
      justifyContent: 'center',
      cursor: 'pointer',
      paddingLeft: '5px',
      paddingRight: '5px',
      fontWeight: '900',
      textTransform: 'uppercase',
      padding: '20px',
    },

    [theme.breakpoints.up('sm')]: {
      cursor: 'pointer',
      justifyContent: 'center',
      alignItems: 'center',
      textAlign: 'center',
      fontSize: '72px',
    },
    [theme.breakpoints.up('md')]: {
      fontSize: '96px',
    },
    [theme.breakpoints.up('xl')]: {
      fontSize: '118px',
    },
  },
}));

const Overlay = ({ isOpen }) => {
  // const [open, set] = useState(false);

  const classes = useStyles();
  const items = [`home`, `about`, `contact`];

  const springRef = useRef();
  const props = useSpring({
    config: config.default,
    to: {
      height: '100vh',
      width: isOpen ? '100vw' : '0vw',
    },
  });

  const trailRef = useRef();
  const trail = useTrail(items.length, {
    to: { opacity: isOpen ? 1 : 0, x: isOpen ? 0 : 60 },
  });

  useChain([springRef, trailRef]);

  return (
    <animated.div
      style={{ ...props, backgroundImage: `url(${background})` }}
      className={classes.root}
    >
      <ul className={classes.items}>
        <Container maxWidth="xs">
          {trail.map((element, i) => {
            const item = items[i];
            return (
              <animated.div
                style={{ ...element, color: '#8167a9', margin: '5px' }}
                key={item}
              >
                {item}
              </animated.div>
            );
          })}
        </Container>
      </ul>
    </animated.div>
  );
};

export default Overlay;
