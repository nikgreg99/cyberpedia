import React from "react";
import {Container,Row,Col,FormControl,InputGroup} from 'react-bootstrap';
import {FaSearch} from 'react-icons/fa';
import { Helmet } from "react-helmet";
import styles from './Home.css';


const Home = () => {
    return <>
        <Helmet>
            <title>Cyberpedia - Home</title>
        </Helmet>
        <Container>
            <Row className="heigth d-flex justify-content-center align-items-center">
                <Col md={6}>
                    <div className={styles}>
                        <FaSearch className="search-icon"/>
                        <InputGroup>
                            <FormControl type="text" placeholder="Search IOC"/>
                        </InputGroup>
                    </div>
                </Col>
            </Row>
        </Container>
    </>
};

export default Home;