import React from "react";
import { Helmet } from "react-helmet";
import NavBar from "../components/Navbar";
import Footer from "../components/Footer";

const MainLayout = ({children}) => {
    return <>
        <Helmet>
            <meta charset='utf-8'/>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'/>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        </Helmet>
        <NavBar/>
        <main>{children}</main>
        <Footer/>
    </>
};

export default MainLayout;
