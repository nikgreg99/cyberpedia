import React from "react";
import { Link } from "react-router-dom";
import { Navbar as BootstrapNavBar, Nav,  NavDropdown, Form, FormControl, Button} from "react-bootstrap";
import logo from '../assets/img/logo_short.png';

const NavBar  = () => {

    return <>
        <BootstrapNavBar className="text-white" bg="dark" variant="dark" expand="lg">
        <div className="container-fluid">
            <BootstrapNavBar.Brand>
                <img
                 src={logo}
                 width="15%"
                 height="15%"
                 alt="logo not found"
                /> &nbsp;
            </BootstrapNavBar.Brand>
            <BootstrapNavBar.Toggle aria-controls="navbar"/>
             <BootstrapNavBar.Collapse id="navbar">
                <Nav className="me-auto mb-2 mb-lg-0">
                    <Nav.Link as={Link} to="/" active>Cyberpedia</Nav.Link>
                    <Nav.Link as={Link} to="/about">About</Nav.Link>
                    <NavDropdown title="IOC" id="ioc-type-dropdown">
                        <NavDropdown.Item as={Link} to="ioc/ips" >IP Addresses</NavDropdown.Item>
                        <NavDropdown.Item as={Link} to="ioc/domains">Domains</NavDropdown.Item>
                        <NavDropdown.Item as={Link} to="ioc/URL">URL</NavDropdown.Item>
                        <NavDropdown.Item as={Link} to="ioc/digests">Digests</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
                <Form className="d-flex" role="search">
                    <FormControl type="search" placeholder="Search IOC"
                     className="me-2" aria-label="Search"/>
                     <Button variant="outline-success">Search</Button>
                </Form>
            </BootstrapNavBar.Collapse>
        </div>
        </BootstrapNavBar>
    </>
};

export default NavBar;