import { Header, Page, MenuItem, Text,
    Logo, AmountCard, Line, TitleCard, TransactionsContainer,
    AmountValue, DepositButton, DraftButton, TransactionsList } from './style';

import LogoTotal from '../../assets/icon/logotype-infinity-bank.svg';

import Transaction from '../../components/Transaction/index';

const Home = () => {
    return(
        <Page>
            <Header>
                <Logo src={LogoTotal}/>
                <MenuItem>
                    <Text>Sobre</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Transações</Text>
                </MenuItem>
                <MenuItem>
                    <Text>Menu</Text>
                </MenuItem>
            </Header>
            <Line>
                <AmountCard>
                    <TitleCard>Saldo</TitleCard>
                    <AmountValue>R$ 20.00</AmountValue>
                </AmountCard>
                <DepositButton type='button'>Depositar</DepositButton>
                <DraftButton type='button'>Sacar</DraftButton>
            </Line>
            <Line>
                <TransactionsContainer>
                    <TitleCard>Transações</TitleCard>
                    <TransactionsList>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                        <Transaction></Transaction>
                    </TransactionsList>
                    
                </TransactionsContainer>
            </Line>
        </Page>
    )
}

export default Home;