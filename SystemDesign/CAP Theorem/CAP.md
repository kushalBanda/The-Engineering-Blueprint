## What is CAP Theorem?

Pick two out of three. That's the CAP theorem in one sentence.

When you're building a distributed system with multiple servers, you can only guarantee two of these three properties:

- **Consistency (C):** All nodes see the same data at the same time
- **Availability (A):** Every request gets a response, even if some nodes are down
- **Partition Tolerance (P):** The system keeps working even when network failures split your servers

Eric Brewer introduced this theorem in 2000, and it's shaped how we think about distributed databases ever since.

![](https://miro.medium.com/v2/resize:fit:888/0*oysFrj9Xo_EacDS0.jpeg)

## The Core Statement

**You can't have all three.** In a distributed system with data replication, you can only guarantee two of the three properties at once. Network failures (partitions) will happen in real systems, so practically you're choosing between consistency and availability.

## Consistency

Every read gets the most recent write. If you write data to node A, then immediately read from node B, you'll get that fresh data—not stale data. All replicas show the same value at the same time.

Example: You update your profile picture. Every server in the cluster immediately reflects this change. No user sees your old picture after the update completes.

**Press enter or click to view image in full size**![img](https://miro.medium.com/v2/resize:fit:1400/1*rf24SbI19r8VHv2C7msjGw.png)

## Availability

Every request gets a response—no failures, no timeouts. Even if some servers are down, the system keeps responding. The response might not have the freshest data, but you'll get an answer.

Example: Amazon's shopping cart stays accessible even during server failures. You can add items to your cart even if some databases are offline. The system prioritizes staying up over perfect consistency.

## Partition Tolerance

The system keeps working when network failures split your servers into isolated groups. If a network cable gets cut and your servers can't talk to each other, the system doesn't crash—it keeps serving requests.

Network partitions aren't hypothetical—they happen in real data centers. A misconfigured router, a failed switch, or a cut fiber cable can split your cluster. Any real distributed system must handle partitions, which is why CAP is really about choosing between consistency and availability when partitions happen.

## The Three Combinations

In practice, you're always picking two. Here's what each combination looks like:

### CA (Consistency + Availability)

Consistent and always available—but only works if your network never fails. This combination is a myth for distributed systems. If network partitions can happen (and they will), you can't have both consistency and availability.

**Production reality:** True CA systems don't exist in distributed databases. Traditional single-server SQL databases (PostgreSQL on one machine) are CA, but they're not distributed. Once you add replication across servers, network failures become possible, and you're forced to choose between C and A.

![img](https://miro.medium.com/v2/resize:fit:1400/1*rf24SbI19r8VHv2C7msjGw.png)


### AP (Availability + Partition Tolerance)

The system stays online during network failures, but different nodes might show different data. If servers can't talk to each other, they keep accepting writes independently. Users get responses, but those responses might be stale.

**When to use:** Shopping carts, social media feeds, DNS, content delivery. Anything where it's more important to stay online than to show perfectly fresh data.

**Production reality:** Amazon DynamoDB, Cassandra, CouchDB. Amazon's shopping cart is the classic example—they'd rather let you add items to a slightly stale cart than show you an error page. Eventual consistency is acceptable because you can fix conflicts later.

![](https://miro.medium.com/v2/resize:fit:1400/1*nxjmKwMUq6TQPst_2k14aA.png)

### CP (Consistency + Partition Tolerance)

The system stays consistent during network failures, but some nodes might become unavailable. If servers can't communicate, they refuse to serve potentially stale data. Users might get errors or timeouts instead of wrong answers.

**When to use:** Banking, payment processing, inventory management. Anything where wrong data is worse than no data. You can't let someone withdraw money twice or oversell a product.

**Production reality:** MongoDB (in certain configurations), HBase, Google Spanner (sort of—it uses clever tricks to get near-CA behavior). Financial systems choose CP—banks would rather show you an error than display the wrong account balance.

The key insight: if you're building a distributed system, network partitions will happen. So you're really choosing between AP (eventual consistency, always available) and CP (strong consistency, might be unavailable).

![](https://miro.medium.com/v2/resize:fit:1400/1*zYwslfbO4oGsS5Yi9DFbIg.png)

## Why This Matters

CAP forces you to make an explicit choice about your system's behavior during failures. You can't have it all, so decide what your users need most:

- **Banks need consistency:** Showing wrong account balances is worse than showing an error message
- **Social media needs availability:** Users expect Instagram to work even if some servers are down. Slightly stale feeds are fine
- **E-commerce is mixed:** Product catalog can be AP (eventual consistency), but inventory and payments should be CP (strong consistency)

Most systems mix approaches—use CP for critical data and AP for everything else.

## Production Examples

**AP Systems (Eventual Consistency, Always Available):**

- **Amazon DynamoDB:** Replicates across availability zones. During network failures, different replicas might temporarily disagree, but the system stays online. Eventual consistency is the default, though you can opt into stronger consistency at a performance cost.
- **Cassandra:** Designed for high availability. Writes succeed as long as some replicas are reachable. You might read stale data temporarily, but the system never goes down.
- **DNS:** The internet's phone book is eventually consistent. DNS changes take time to propagate, but lookups always work.

**CP Systems (Strong Consistency, Might Be Unavailable):**

- **Google Spanner:** Uses atomic clocks and GPS to synchronize time across data centers. Achieves strong consistency globally but can become unavailable during partitions. Google pays big money for the hardware to make this work.
- **MongoDB (with majority write concern):** Writes only succeed if most replicas acknowledge them. During partitions, minority replicas become read-only.
- **Zookeeper/etcd:** Configuration stores that prioritize consistency. Used for critical coordination tasks like leader election. They'd rather be unavailable than serve wrong data.

The pattern: AP wins for user-facing features (social feeds, recommendations, content). CP wins for critical operations (payments, inventory, coordination).

