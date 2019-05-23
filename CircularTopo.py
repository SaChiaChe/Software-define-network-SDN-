from mininet.topo import Topo

class MyTopo (Topo):
 #"Simple topology example."

	def __init__ (self):
		#"Create custom topo."
		# Initialize topology
		Topo.__init__(self)

		# Add hosts an switches
		Host1 = self.addHost('h1')
		Host2 = self.addHost('h2')
		Host3 = self.addHost('h3')
		Host4 = self.addHost('h4')
		Switch1 = self.addSwitch('s1')
		Switch2 = self.addSwitch('s2')
		Switch3 = self.addSwitch('s3')
		Switch4 = self.addSwitch('s4')

		# Add links
		self.addLink(Host1, Switch1)
		self.addLink(Host2, Switch2)
		self.addLink(Host3, Switch3)
		self.addLink(Host4, Switch4)
		self.addLink(Switch1, Switch3)
		self.addLink(Switch1, Switch4)
		self.addLink(Switch2, Switch3)
		self.addLink(Switch2, Switch4)

topos = {'mytopo':(lambda: MyTopo())}