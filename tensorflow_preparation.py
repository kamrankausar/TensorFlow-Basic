
# coding: utf-8

# In[1]:


# See tensorflow version


# In[3]:


get_ipython().system('pip list | grep tensorflow')


# In[1]:


# install some particular version
get_ipython().system('pip install tensorflow==1.11.0 ')


# In[2]:


# Import and use TensorFlow


# In[3]:


import tensorflow as tf


# In[4]:


hello = tf.constant('Hello, TensorFlow!')


# In[5]:


sess = tf.Session()


# In[6]:


print(sess.run(hello))

