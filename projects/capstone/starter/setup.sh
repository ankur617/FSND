#!/bin/bash
export DATABASE_URL="postgresql://postgres@localhost:5432/postgres"
export EXCITED="true"
export token_executive_producer="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkttcUhyR2pYYUlBNGJ2eGN5YTZRcyJ9.eyJpc3MiOiJodHRwczovL2Fua3VyNjE3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MjdmNzJiZjlkMDQyYzAwNjkzOTE3NTUiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNjU3OTY0NDU4LCJleHAiOjE2NTc5NzE2NTgsImF6cCI6IlZuUlBOb2lSNVVsNk5HVE1qRXQ0eE9uVkVNdnA3VXdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.LrNOojxRS0ApY6rJ2ogrhEU4jR66KswEAKeNc1tXqhEq23VgKxpkw_n2J9BfgSSdzYDioStGFj9VHQ-MU_xCfeJA9xvrfYA6X8XM8R-SYLgnHTxtT3rkmNRPvzDYlebdSurwZrVDR2qLYstoC_qvX9eRS8fr2Aj1N5h1i888wyQ8zlXDCXX988nPpsKW6qHY1k5MqDaaIa_qjXrE20o92RnMS93bBoG413jlYBP5wrmC2DTNed9zk6TgIsMKD3Tf8NRt_XRYxn1eqJfUrGrS5v5vgKumjplI5l3pYjxqC2ElpQNHKCzQ1yBV4NOS49_P0qf-nhQKbCYezn4-0Z9NHQ"
export token_casting_assitant="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkttcUhyR2pYYUlBNGJ2eGN5YTZRcyJ9.eyJpc3MiOiJodHRwczovL2Fua3VyNjE3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmNhZDAyOTQxODE0Njc1YTU5MDQxNDgiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNjU3OTY0NTEwLCJleHAiOjE2NTc5NzE3MTAsImF6cCI6IlZuUlBOb2lSNVVsNk5HVE1qRXQ0eE9uVkVNdnA3VXdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.f-bOnvJhBoGxiR_ZFMswAgVuxXrKyNxkGXcGQDpZWcDpgNUo5TrgExBuaIxF-uzEfoof9kUA6Pukozxo0XEXst_j_fohF562TWgh5r7x8Ij-6MaSquxwwiHdU_7RNxESy0iXfNvFZVun9KxVxYCr19kYwi7ZGQ86XjItvCl19HX-17HLF7fqf4Ow_9jtSQJktGXpL1RJrKtLyQQMflx1jDMt8M3QnHFSSjt9GSWqoB4FJjYjtIWqSL_R1_3IpfB7YGLdm-ERU4e1N6kecCeCe_CxNrVsFQ8scZ87kpdfqehNPZrKCCVPNTXegqBcCdL8MiwATDlJm_gSyT2_V0QZaA"
export token_casting_director="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkttcUhyR2pYYUlBNGJ2eGN5YTZRcyJ9.eyJpc3MiOiJodHRwczovL2Fua3VyNjE3LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2Mjc2MGEzMDA0YjBmYTAwNjkyZmVhYzEiLCJhdWQiOiJjYXN0aW5nYWdlbmN5IiwiaWF0IjoxNjU3OTY1MTM3LCJleHAiOjE2NTc5NzIzMzcsImF6cCI6IlZuUlBOb2lSNVVsNk5HVE1qRXQ0eE9uVkVNdnA3VXdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.MtNqHahR7pg27oM3QEr0yBrzHykcvlXUDEfQngNFci03ksgmyPG4oZTaqClpz3kJHIMh4hGvnxxlws3MS98HicrtCe2C6haqnZ7jSCp3vkZZWYcrA7Mce3_bnwAdLHjoiwsjQWBazxPT0eNq634WrJfpouEcbXDh1eaQqMuFAxCG-tLd7CdzjJMAdkakuD4fg1i3cAZpbid4ToKZA1eyJXMxhWtIPgMws-Ilw53Xzoj7vXHfjOX1Rb98tFV0WvYYx7mPdWojQW0TRBqp6ZUxPxELgcrprAVaE7Q95Q7K81gzIIRJCex3zdQupRZSzm5eWaZyAciANdjvpthhjCwd1A"
echo "setup.sh script executed successfully!"
