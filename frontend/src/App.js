import React from 'react';
import MainLayout from './templates/MainLayout';
import Home from './pages/Home';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import 'bootstrap/dist/js/bootstrap.bundle';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  return <>
    <BrowserRouter>
      <MainLayout>
          <Routes>
            <Route exact path='/' Component={Home}/>
          </Routes>
        </MainLayout> 
    </BrowserRouter>
  </>
}

export default App;
