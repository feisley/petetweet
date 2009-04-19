// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class RegisterEvent extends Event
	{
		public function RegisterEvent(username:String, password:String, cpassword:String, 
		firstname:String, lastname:String, email:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("RegisterEvent", bubbles, cancelable);
			
			this.username = username;
			this.password = password;
			this.cpassword = cpassword;
			this.firstname = firstname;
			this.lastname = lastname;
			this.email = email;
		}
		
		public var username:String;
		public var password:String;
		public var cpassword:String;
		public var firstname:String;
		public var lastname:String;
		public var email:String;
		
		override public function clone():Event {
			return new RegisterEvent(username, password, cpassword, firstname,lastname,email);
		}
		
	}
}