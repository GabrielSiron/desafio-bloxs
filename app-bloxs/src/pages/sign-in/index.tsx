import React ,{ useState, useContext, useEffect} from 'react';
import { UserContext } from '../../contexts/user';
import { AuthPage, AuthSide, WelcomeContainer, AuthTitle, AuthSubTitle, Form, 
  ActionButton } from '../../styles/main-auth-structure';
import { Img } from './style'
import InputComponent from '../../components/Input/index';
import { Login }from '../../services/auth/index'
import Logo from '../../assets/icon/infitity-bank-mark.svg';
import { useNavigate } from 'react-router-dom';

const SignIn = () => {
  const { email, password, token, setToken, setEmail, setPassword } = useContext(UserContext);

  const Auth = async () => {
    await Login({email, password}, setToken);
    
  }
  
  let navigate = useNavigate();

  useEffect(()=>{
    
    if(token.length > 0){
        navigate('/home')
    }
  })

  return(
    <AuthPage>
      <AuthSide>
        <WelcomeContainer>
          <Img src={Logo}/>
          <AuthSubTitle>Login</AuthSubTitle>
        </WelcomeContainer>
        <Form>
          <InputComponent inputType={'email'}/>
          <InputComponent inputType={'password'}/>
          <ActionButton type='button' onClick={Auth} disabled={false}>Criar Conta</ActionButton>
        </Form>
      </AuthSide>
    </AuthPage>
  )
}
export default SignIn;