import React from "react";
import styled from "styled-components";
import { makeStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Toolbar from "@material-ui/core/Toolbar";
import { useQuery } from "@apollo/client";
import { ALL_COURSES, STUDENT_DETAILS } from "../components/Dashboard/Queries";
// import { useParams } from 'react-router-dom';
import Layout, {
  Root,
  getHeader,
  getDrawerSidebar,
  getSidebarTrigger,
  getSidebarContent,
  getCollapseBtn,
  getContent,
  getFooter,
} from "@mui-treasury/layout";
import { HeaderMockUp } from "@mui-treasury/mockup/layout";
import { TextSidebar } from "@mui-treasury/mockup/sidebars";
import Sidebar from "../components/Dashboard/Sidebar";
import { initializeApollo } from "../lib/apolloClient";

import HomeAlt from "./dashboard/home";

const Header = getHeader(styled);
const DrawerSidebar = getDrawerSidebar(styled);
const SidebarTrigger = getSidebarTrigger(styled);
const SidebarContent = getSidebarContent(styled);

const Content = getContent(styled);

const scheme = Layout();

scheme.configureHeader((builder) => {
  builder.registerConfig("xs", {
    position: "sticky",
  });
});

scheme.configureEdgeSidebar((builder) => {
  builder
    .create("primarySidebar", { anchor: "left" })
    .registerTemporaryConfig("xs", {
      anchor: "left",
      width: "40vw",
    })
    .registerTemporaryConfig("sm", {
      anchor: "left",
      width: "20vw",
    })
    .registerPermanentConfig("lg", {
      width: "12vw",
      persistentBehavior: {
        whatever_id: "fit",
        _others: "none",
      },
    });
});

const useStyles = makeStyles(() => ({
  header: {
    backgroundColor: "#F0F0F3",
  },
  collapseBtn: {
    color: "#fff",
    minWidth: 0,
    width: 40,
    borderRadius: "50%",
    border: "none",
    backgroundColor: "rgba(0,0,0,0.24)",
    margin: "0 auto 16px",
    "&:hover": {
      backgroundColor: "rgba(0,0,0,0.38)",
    },
  },
  sidebar: {
    backgroundColor: "#00293B",
    border: "none",
  },
  content: {
    backgroundColor: "#F0F0F3",
  },
}));

function renderPage(page) {
  console.log(page);
  switch (page) {
    case "home":
      return <HomeAlt />;
    case "timetable":
      return <HomeAlt />;
    default:
      return <HomeAlt />;
  }
}

const Dashboard = () => {
  const styles = useStyles();
  const { loading, data, error } = useQuery(STUDENT_DETAILS, {
    variables: {
      user: "VXNlck5vZGU6MQ==",
    },
  });
  if (loading) {
    console.log(loading);
  }
  if (data) {
    console.log(data);
  }
  // const { page } = useParams();
  return (
    <Root scheme={scheme}>
      <CssBaseline />
      <Header className={styles.header}>
        <Toolbar>
          <SidebarTrigger sidebarId="primarySidebar" />
          <HeaderMockUp />
        </Toolbar>
      </Header>
      <DrawerSidebar
        sidebarId="primarySidebar"
        PaperProps={{ className: styles.sidebar }}
      >
        <SidebarContent>
          {/* <TextSidebar /> */}
          <Sidebar />
        </SidebarContent>
        {/* <CollapseBtn className={cx(styles.collapseBtn)} /> */}
      </DrawerSidebar>
      <Content className={styles.content}>{renderPage("home")}</Content>
    </Root>
  );
};

export async function getServerSideProps() {
  const apolloClient = initializeApollo();

  await apolloClient.query({
    query: ALL_COURSES,
  });
  await apolloClient.query({
    query: STUDENT_DETAILS,
    variables: {
      user: "VXNlck5vZGU6MQ==",
    },
  });

  return {
    props: {
      initialApolloState: apolloClient.cache.extract(),
    },
  };
}

export default Dashboard;
