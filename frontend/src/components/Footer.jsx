import React  from "react";
import { Container, Row, Col} from "react-bootstrap";
import {FaHome} from 'react-icons/fa'
import {IoMdMail} from 'react-icons/io';
import {BsTelephoneFill} from 'react-icons/bs';


const Footer = () =>{

    const currentYear = new Date().getFullYear();

    return <>
        <footer className="text-white text-center text-lg-start" 
            style={{backgroundColor: '#23242a'}}>
            <Container className="p-4">
                <Row className="mt-4">
                    <Col lg={4} md={12} mb={4} mb-mb={0}>
                        <h5 className="text-uppercase mb-4">About Eclexys</h5>
                        <p>
                            Safeguard your enterprise with EcLexys Extended Firewalling System (EXYS-EFS). Our 
                            versatile solution delivers robust protection against diverse network threats, from SQL injections to denial-of-service attacks, 
                            ensuring the security of your corporate perimeter.
                        </p>
                    </Col>
                    <Col lg={4} md={6} mb={4} mb-md={0}>
                        <h5 className="text-uppercase mb-4 pb-1">Our contacts</h5>
                        <ul style={{marginLeft: '1.65em', listStyle: "none"}}>
                            <li className="mb-3">
                                <FaHome/>
                                <span className="ms-2">Via dell'Inglese 6</span>
                                <span className="ms-2">CH-6826 Riva San Vitale</span>
                                <span className="ms-2">Switzerland</span>
                            </li>
                            <li className="mb-3">
                                <IoMdMail/>
                                <span className="ms-2">office@eclexys.com</span>
                            </li>
                            <li className="mb-3">
                                <BsTelephoneFill/>
                                <span className="ms-2">+41 91 600 000</span>
                            </li>
                        </ul>
                    </Col>
                </Row>
            </Container>
            <div className="text-center p-3">
                &copy; {currentYear} Copyright&nbsp;
                <a style={{textDecoration: 'none'}} className="text-white" href="https://eclexys.com/">Eclexys Sagl</a> All rights reserved
            </div>
        </footer>
    </>;

}

export default Footer;