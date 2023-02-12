import React ,{ useContext, useEffect} from 'react';
import { UserContext } from '../../contexts/user';
import { AuthPage, FormContainer, WelcomeContainer, GoToRegistry, AuthSubTitle, Form, 
  ActionButton } from '../../styles/main-auth-structure';
import { Img } from './style'
import InputComponent from '../../components/Input/index';
import { Login }from '../../services/auth/index'
import Logo from '../../assets/icon/infitity-bank-mark.svg';
import { useNavigate } from 'react-router-dom';

const SignIn = () => {
  const { email, password, token, setToken } = useContext(UserContext);

  const Auth = async () => {
    await Login({email, password}, setToken);
    
  }

  const routeChange = () =>{ 
    let path = `/signup`; 
    navigate(path);
  }
  
  let navigate = useNavigate();

  useEffect(()=>{
    
    if(token.length > 0){
        navigate('/home')
    }
  })

  return(
    <AuthPage>
      <FormContainer>
        <WelcomeContainer>
          <Img src={Logo}/>
          <AuthSubTitle>Login</AuthSubTitle>
        </WelcomeContainer>
        <Form>
          <InputComponent inputType={'email'}/>
          <InputComponent inputType={'password'}/>
          <ActionButton type="button" onClick={Auth} >Fazer Login</ActionButton>
          <GoToRegistry type="button" onClick={routeChange}>Não tem conta? Se inscreva!</GoToRegistry>
        </Form>
      </FormContainer>
    </AuthPage>
  )
}
export default SignIn;