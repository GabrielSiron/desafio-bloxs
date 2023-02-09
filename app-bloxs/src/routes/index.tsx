import  { UserContext }  from '../contexts/user';
import React, { useState, useEffect } from 'react';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import SignUp from '../pages/sign-up/index';
import SignIn from '../pages/sign-in/index';
import Home from '../pages/home/index';

export const AppRoutes = ()=>{
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [token, setToken] = useState('');
    const [name, setName] = useState('');
    const [cpf, setCpf] = useState('');
    return(
        <Router>
            <UserContext.Provider value={{email, setEmail, password, setPassword, token, setToken, name, setName, cpf, setCpf}}>
                    <Routes>
                        <Route path='/signup' element={<SignUp />}/>
                        <Route path='/signin' element={<SignIn />}/>
                        <Route path='/home' element={<Home />}/>
                    </Routes>
            </UserContext.Provider>
        </Router>
    );
}