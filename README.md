# PriorityQueue
<h2>This is a python package for PriorityQueue which performs all the priority queue operations on objects and non objects..</h2>
<p>Here we have a PriorityQueue class which User can import and create an object of that particular class.By default the class performs operations in ascending order and for non objects. </p>
 <h4>Sample Code</h4>
 <h5>Creating a PriorityQueue class</h5>
 <h6>A PriorityQueue object for non objects and performs minHeap operations.</h6>
 <p>pq=PriorityQueue()</p>
 <h6>PriorityQueue object that performs minHeap Operations on objects</h6>
 <p>pq=PriorityQueue(withObject=True)</p>
 <h6>A PriorityQueue object for non objects and performs maxHeap operations</h6>
 <p>pq=PriorityQueue(descending=True)</p>
<h6>A PriorityQueue object for objects and performs maxHeap operations</h6>
<p>pq=PriorityQueue(descending=True,withObject=True)</p>
<h3>PriorityQueue Methods</h3>
<h4>add(key,value)-Method to add to the priority queue</h4>
<p>key- The primitive value for non objects (or) the object parameter value through which we want to compare the objects.</p>
<p>value-By default the value is none which is used for non objects(or) we can pass the object as value if we want to compare objects.</p>
<h4>peek()-Method that returns the top element and does not remove it</h4>
<h4>poll()-Method that returns the top elements and removes it</h4>
<h4>len()-method that returns the size of priority queue</h4>
<p>pq=PriorityQueue()</p>
<p>len(pq)</p>
<h4>isEmpty()-Method that returns whether the priority queue is empty or not</h4>
