import * as React from "react"
import {
  ChakraProvider,
  Box,
  Text,
  Link,
  VStack,
  Code,
  Grid,
  theme,
  Center, 
  Flex
} from "@chakra-ui/react"
import { ColorModeSwitcher } from "./ColorModeSwitcher"
import { Logo } from "./Logo"
import { LoginButton } from './components/LoginButton'
import { LogoutButton } from './components/LogoutButton'
import { Routes, Route } from 'react-router-dom'
import { MainPage } from './pages/MainPage'

export const App = () => (
    <ChakraProvider theme={theme}>
      <Flex h='100vh' w='100vw'>
        <Center bg='green.400' h='100%' color='white' w='full'>
          <LoginButton mr={12}/>
          <LogoutButton />
          <Routes>
            <Route path="/main" element={<MainPage />} />
          </Routes>
        </Center>
      </Flex>
    </ChakraProvider>  
)
