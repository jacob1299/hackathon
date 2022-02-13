import { ColorModeScript } from "@chakra-ui/react"
import * as React from "react"
import ReactDOM from "react-dom"
import { App } from "./App"
import { ChakraProvider } from '@chakra-ui/react'
import { Auth0Provider } from '@auth0/auth0-react'
import { BrowserRouter } from 'react-router-dom'

const domain = process.env.REACT_APP_AUTH0_DOMAIN
const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID

ReactDOM.render(
  <BrowserRouter>
    <Auth0Provider domain={domain as string} clientId={clientId as string} redirectUri={window.location.origin}>
      <ChakraProvider >
      <React.StrictMode>
        <ColorModeScript />
        <App />
      </React.StrictMode>
    </ChakraProvider >
    </Auth0Provider>
  </BrowserRouter>
  ,
  document.getElementById("root"),
)
