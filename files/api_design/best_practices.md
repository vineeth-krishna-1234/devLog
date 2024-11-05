
# Best practice to be followed in REST apis


- Accept and Respond in JSON
- use nouns instead for verbs when naming routes
```
Eg: /articles, /users and not /get_users /get_articles
```
- Use logical nesting on endpoints
```
Eg : 
/products/{productId}/reviews/{reviewId}
/authors/{authorId}/posts/{postId}
```
- Handle errors gracefully and return standard error codes
- Allow filtering, sorting, and pagination
```
Eg:
/employees?lastName=Smith&age=30
http://example.com/articles?sort=+author,-datepublished
```
- Maintain good security practices
```
SSL/TLS certificates
Access control 
```
- Cache data to improve performance
- Versioning our APIs
```
use /v1 /v2 ... so on routes for versioning
```





---
GET -  retrieves a representation of the resource at the specified URI. The body of the response message contains the details of the requested resource.

POST - creates a new resource at the specified URI. The body of the request message provides the details of the new resource. Note that POST can also be used to trigger operations that don't actually create resources.

PUT - either creates or replaces the resource at the specified URI. The body of the request message specifies the resource to be created or updated.

PATCH - performs a partial update of a resource. The request body specifies the set of changes to apply to the resource.

DELETE - removes the resource at the specified URI.

---


PUT - Behavior: All fields in the resource should be included in the request, as any missing fields will typically be set to their defaults or null.

PATCH - Behavior: Only the provided fields are updated, leaving other fields as they are.

---

HATEOAS (Hypermedia as the Engine of Application State) is a constraint of the REST (Representational State Transfer) architecture that enables a more dynamic, discoverable API by embedding hyperlinks within responses. These links allow clients to navigate the API by following links relevant to the resource they’re interacting with, without needing to know endpoints in advance.

```
Eg:
{
  "id": 123,
  "name": "Smartphone",
  "price": 499.99,
  "inStock": true,
  "links": [
    {
      "rel": "self",
      "href": "/products/123"
    },
    {
      "rel": "add-to-cart",
      "href": "/cart",
      "method": "POST"
    },
    {
      "rel": "reviews",
      "href": "/products/123/reviews",
      "method": "GET"
    },
    {
      "rel": "similar-products",
      "href": "/products/123/similar",
      "method": "GET"
    }
  ]
}
```