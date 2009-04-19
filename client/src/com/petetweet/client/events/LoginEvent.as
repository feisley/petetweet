// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class LoginEvent extends Event
	{
		public function LoginEvent(username:String, password:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("LoginEvent", bubbles, cancelable);
			
			this.username = username;
			this.password = password;
		}
		
		public var username:String;
		public var password:String;
		
		override public function clone():Event {
			return new LoginEvent(username, password);
		}
		
	}
}