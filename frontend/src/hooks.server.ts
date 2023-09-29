import { SvelteKitAuth } from "@auth/sveltekit"
import GitHub from "@auth/core/providers/github"
import { GITHUB_ID, GITHUB_SECRET,LDAP_URI } from "$env/static/private"
import CredentialsProvider from "@auth/core/providers/credentials"
import ldap from "ldapjs";

/*
export const handle = SvelteKitAuth({
  providers: [GitHub({ clientId: GITHUB_ID, clientSecret: GITHUB_SECRET })],
})
*/

const client = ldap.createClient({
  url: LDAP_URI,
})

client.on('connectError', (err) => {
  console.error('LDAP client connection error', err)
})

export const handle = SvelteKitAuth({

  providers: [
    CredentialsProvider({
      name: "LDAP",
      credentials: {
        username: { label: "DN", type: "text", placeholder: "" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials, req) {
        return new Promise((resolve, reject) => {
          client.bind(credentials.username, credentials.password, (error) => {
            console.log("Attempting to log in as", credentials.username)
            if (error) {
              console.error("Failed")
              //reject()
              resolve(
                {
                  username: credentials.username,
                  password: credentials.password,
                }
              )
            } else {
              console.log("Logged in")
              resolve({
                username: credentials.username,
                password: credentials.password,
              })
            }
          })
        })
      },
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      const isSignIn = user ? true : false
      if (isSignIn) {
        token.username = user.username
        token.password = user.password
      }
      return token
    },
    async session({ session, token }) {
      return { ...session, user: { username: token.username } }
    },
  }
})